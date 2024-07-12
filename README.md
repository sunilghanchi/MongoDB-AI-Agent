# MongoDB-AI-Agent

A Python-based AI agent designed to interact with MongoDB using natural language queries. This project leverages the Groq API and provides a user-friendly interface built with Streamlit. Simply input your query in natural language, and the agent will return the results in a chat format.

## Features

- Natural language query processing
- Chat format response
- Streamlit interface for easy interaction
- Integration with MongoDB via the Groq API

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- MongoDB
- Groq API access

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sunilghanchi/MongoDB-AI-Agent.git
    ```
2. Navigate to the project directory:
    ```bash
    cd MongoDB-AI-Agent
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Prepare your prompt template and sample queries:
    - `prompt.txt`: Template file for the AI agent prompts
    - `sample.txt`: File containing sample queries

2. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

3. Open the Streamlit interface in your browser:
    ```
    http://localhost:8501
    ```

4. Enter your query in natural language and receive the results in chat format.

## Files

- `main.py`: Main application file for running the Streamlit interface
- `requirements.txt`: List of dependencies required for the project
- `prompt.txt`: Template file for the AI agent prompts
- `sample.txt`: Sample query file

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Groq API](https://groq.com/)
- [MongoDB](https://www.mongodb.com/)
