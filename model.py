from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import ctransformers
from langchain.chains import RetrievalQA

import chainlit as cl


DB_FAISS_PATH = "vectorstores/db_faiss"


input_variables = ["Context", "question"]


custom_prompt_template = """Use the following pieces of information to answer the user's question.


Context = {Context}

Question = {question}



only returns the helpful answer below and nothing else

Helpful answer

"""


def set_custon_prompt():

    prompt = PromptTemplate(template=custom_prompt_template,

                            input_variables=input_variables,

                            validate_variable_names=False)

    return prompt


def load_llm():

    llm = ctransformers.CTransformers(

        # old model = llama-2-7b-chat.ggmlv3.q8_0.bin
        model="llama-2-7b-chat.ggmlv3.q4_0.bin",

        model_type='llama',

        max_new_tokens=512,

        temperature=0.5

    )

    return llm


def retrival_qa_chain(llm, prompt, db):

    qa_chain = RetrievalQA.from_chain_type(

        llm=llm,

        chain_type="stuff",

        retriever=db.as_retriever(search_kwargs={"k": 2}),



        return_source_documents=True,

        chain_type_kwargs={'prompt': prompt, 'document_variable_name': 'Context'}

    )

    return qa_chain


def qa_bot():

    embeddings = HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

    db = FAISS.load_local(DB_FAISS_PATH, embeddings)

    llm = load_llm()

    qa_prompt = set_custon_prompt()

    qa = retrival_qa_chain(llm, qa_prompt, db)

    return qa


def final_result(query):

    qa_result = qa_bot()

    response = qa_result({'query': query})

    return response


### Chain LIT ###

@cl.on_chat_start
async def start():

    chain = qa_bot()

    cl.user_session.set("chain", chain)

    msg = cl.Message(content="Starting the bot.....")

    await msg.send()

    msg.content = "Hi, What is your query?"

    await msg.update()


@cl.on_message
async def main(message):

    chain = cl.user_session.get("chain")

    cb = cl.AsyncLangchainCallbackHandler(

        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]



    )

    cb.answer_reached = True

    res = await chain.acall(message, callbacks=[cb])

    answer = res['result']

    sources = res['source_documents']

    if sources:

        answer += f"\nSources: " + str(sources)

    else:

        answer += f"\nSources: No sources found"

    await cl.Message(content=answer).send()
