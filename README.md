# AI Chat Bot

A high-performance, asynchronous AI chatbot architecture powered by **FastAPI**, orchestrated with **LangChain**, and accelerated using **Groq** cloud inference engines.

## 🚀 Features

* **⚡ Ultra-Fast Inference**: Integrated with [Groq Cloud](https://groq.com) for lightning-fast token generation using open-source models.
* **🦜 Orchestrated Workflows**: Powered by [LangChain](https://langchain.com) to easily manage chat templates, history tokens, and LLM chains.
* **🚀 Asynchronous REST API**: Powered by [FastAPI](https://tiangolo.com) providing robust, non-blocking asynchronous `/chat` endpoints.
* **📱 Clean Frontend UI**: A modular web interface developed by Nishant (`index.html`) providing seamless event rendering.

## 📂 Project Structure

```text
├── agent.py         # LangChain logic, ChatGroq initialization, and prompt templates
├── main.py          # FastAPI app instance, CORS configurations, and API routes
├── index.html       # Web client UI frontend (Created by Nishant)
├── requirements.txt # Project dependency specifications
└── .gitignore       # System file exclusions
```

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.9+
* A **Groq API Key** (Get one for free at the [Groq Console](https://groq.com))

### 1. Clone & Navigate
```bash
git clone https://github.com
cd chat_bot
```

### 2. Configure Your Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate environment (Windows)
.\venv\Scripts\activate

# Activate environment (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory of your project to securely store your keys:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

## 💻 Usage

1. Start your local FastAPI backend server with `uvicorn`:
   ```bash
   uvicorn main:app --reload
   ```
2. Open `index.html` directly in your browser or serve it via a local static web host to begin interacting with your Groq-powered LangChain agent.

## 👥 Contributors

* **codemaster010pro** - Backend, API logic, and Agent engineering.
* **Nishant** - Frontend architecture and Web UI layout.

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:
1. **Fork** the repository.
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`).
4. **Push** the branch up to GitHub (`git push origin feature/AmazingFeature`).
5. **Open** a Pull Request.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Copyright © 2026 codemaster010pro & Nishant.
