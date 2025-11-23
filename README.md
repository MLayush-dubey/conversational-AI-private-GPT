# Conversational AI Private GPT

A full-stack conversational AI web app that enables chat with multiple local and open-source LLMs via a Streamlit interface, with chat history stored in MongoDB. Supports running Ollama models locally or via Docker, with cloud deployment support (Streamlit Cloud).

---

## Features

- **Multi-Model Chat:** Select from multiple LLMs (Llama 3, Deepseek, GPT-OSS, Phi4) for reasoning and conversation.
- **Persistent Chat History:** All conversations are stored/retrieved in MongoDB, organized by title and model.
- **Model Loading:** Uses Ollama to run and manage open-source models locally or in Docker.
- **Frontend:** User-friendly Streamlit app with sidebar history, title search, and instant delete for chats.
- **Cloud Ready:** Easily deployable on Streamlit Cloud or locally with Docker.
- **Extensible Backend:** Modular Python code; add new models, services, or database logic easily.

---

## Getting Started

### Prerequisites

- Python 3.12+
- [Streamlit](https://streamlit.io/)
- [Docker](https://www.docker.com/) (for Ollama container)
- [MongoDB](https://www.mongodb.com/) (local for testing, or remote for cloud deployment)
- [Ollama](https://ollama.com) (for running local/open-source LLMs)

---

### Local Installation

1. **Clone the repository:**
2. **Set up Python environment and install dependencies:**
3. **Configure environment variables:**
- Create a `.env` file in the root with the following:
  ```
  MONGO_DB_URL="YOUR_MONGODB_SERVER"
  MONGO_DB_NAME="NAME_OF_COLLECTION"
  OLLAMA_URL="http://localhost:11434"
  OLLAMA_MODELS="MODELS_AVAILABLE"
  ```

4. **Run MongoDB locally:**  
Make sure MongoDB server is running at `localhost:27017`.

5. **Run Ollama Docker container:**
6. **Start the Streamlit app:**

## Usage

- Launch the web app, select your LLM from the dropdown, and start chatting!
- Access chat history in the sidebar, create new chats, and delete any chat on demand.

---

## Credits

- Powered by [Streamlit](https://streamlit.io/)
- Uses [Ollama](https://ollama.com) for local model inference
- Backend and DB: Python, PyMongo, Pydantic

---

