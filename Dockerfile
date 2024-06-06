# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install virtualenv
RUN pip install virtualenv

# Create and activate virtual environment, install dependencies, and Chainlit
RUN python3 -m venv env && \
    /bin/bash -c "source env/bin/activate && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install chainlit && \
    pip install langchain_community"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run your Python scripts and Chainlit app
CMD /bin/bash -c "source env/bin/activate && \
    python3 downloadLLM.py && \
    python3 ingest.py && \
    chainlit run main.py --host 0.0.0.0 --port 8000"
