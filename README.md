# AskAway - HackUTA 2023 🚀🚀🚀
This project was built for HackUTA 2023 to demonstrate an LLM which can  be trained and ran offline on local host. 

## Developers
 -**Alok Jha**
 -**Ribesh Joshi**
 -**Khushi Gauli**
 -**Kritazya Upreti**


## About the project

This project showcases how a large language model can be fine-tuned on a custom dataset and deployed for low-latency inference completely offline on a local machine.

The project uses the LangChain library to handle data ingestion, model training loops and managing the model lifecycle. The ChainLit framework is used to package and deploy the LLM inference server for easy access through a web UI or APIs.

## Some key aspects:
-**Fine-tunes a small-sized LLM like MiniLM for custom data**
-**Does not require an internet connection after deployment**
-**Low-latency querying against the fine-tuned LLM**
-**Easy to update model as new data comes in**
-**Python implementation allows full customization**

This demonstrates how modern transfer learning techniques can be used to take a pre-trained LLM and specialize it for niche domains and offline usage.

## Usage
-**Give the LLM domain-specific data**
-**Ask natural language questions to get information about the data**