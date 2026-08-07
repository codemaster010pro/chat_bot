# AI Chat Bot

The AI chat bot is built with a performance and asynchronous architecture. It uses FastAPI and LangChain to make it work. The AI chat bot also uses Groq cloud inference engines to make it faster.

## Features

* The AI chat bot can generate tokens quickly. This is because it is integrated with Groq Cloud.

* The AI chat bot has workflows that are powered by LangChain. This makes it easy to manage chat templates, history tokens and LLM chains.

* The AI chat bot has a REST API that's asynchronous. This is made possible by FastAPI. The API has non-blocking asynchronous endpoints for chat.

* The AI chat bot has a frontend UI. Nishant created a web interface that makes it easy to render events smoothly.

## Project Structure

```text

agent.py # this file has the LangChain logic the initialization of ChatGroq and the prompt templates

main.py  # this file has the FastAPI application instance, the CORS configurations and the API routes

index.html       # this is the web client UI frontend that Nishant created

├── requirements.txt # this file has the list of project dependencies

└──.gitignore       # this file has the list of files and folders that the system ignores

```

## Installation & Setup

### Prerequisites

* You need to have Python 3.9 or higher installed.

* You need to have a Groq API Key. You can get one for free from the Groq Console.

### 1.. Navigate

```bash

git clone https://github.com

cd chat_bot

```

### 2. Set Up Your Virtual Environment

```bash

# create an environment

python -m venv venv

# activate the environment on Windows

.\venv\Scripts\activate

# activate the environment on macOS or Linux

source venv/bin/activate

```

### 3. Install Dependencies

```bash

pip install -r requirements.txt

```

### 4. Set Up Environment Variables

You need to create a.env file in the root directory of your project to store your keys securely:

```env

GROQ_API_KEY=gsk_your_actual_groq_api_key_here

```

## Usage

1. Start the FastAPI backend server using uvicorn:

```bash

main:app --reload

```

2. You can open the index.html file directly in your browser. Use a local static web server to serve it. This will allow you to start interacting with your Groq-powered LangChain agent.

## Contributors

* codemaster010pro is responsible for the backend the API logic and agent engineering of the AI chat bot.

* Nishant is responsible for the frontend architecture and the Web UI layout of the AI chat bot.

## Contributing

We welcome contributions to the AI chat bot. Here are the steps to follow:

1. Fork the repository.

2. Create a feature branch.

3. Make your changes. Commit them.

4. Push the branch to GitHub.

5. Open a Pull Request.

## License

The AI chat bot project is covered by the Apache License 2.0. You can find details, in the LICENSE file.

Copyright 2026 codemaster010pro and Nishant.
