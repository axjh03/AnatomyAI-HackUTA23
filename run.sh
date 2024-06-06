#!/bin/bash

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip3 install -r requirements.txt
pip3 install chainlit

# Add virtual environment's bin directory to PATH
export PATH="$PATH:$PWD/env/bin"

# Run your Python scripts and Chainlit app
python3 downloadLLM.py
python3 ingest.py
chainlit run main.py