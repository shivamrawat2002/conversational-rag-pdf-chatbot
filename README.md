# 💬 Conversational RAG PDF Chatbot

> Chat with your PDF documents using AI — with full conversation memory, powered by **Groq LLaMA 3.3 70B** (Free) and **ChromaDB**.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Groq](https://img.shields.io/badge/Groq-Free%20LLM-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorStore-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 What This Does

Upload any PDF and have a **multi-turn conversation** with its content. The app remembers your previous questions within a session — so follow-up questions like *"tell me more about that"* just work.

Built entirely on **free APIs** — no OpenAI subscription needed.

---

## ✨ Features

- 📄 Upload multiple PDFs and chat with their combined content
- 🧠 Session-based memory — context-aware follow-up questions
- ⚡ Groq LLaMA 3.3 70B — fast, free, state-of-the-art LLM
- 🔍 ChromaDB local vector store — your data stays on your machine
- 🆓 HuggingFace embeddings — no paid embedding API needed
- 🔐 API key loaded from `.env` — no key input in the UI
- 💬 Expandable chat history viewer per session

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Groq API — `llama-3.3-70b-versatile` (Free) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` (Free, Local) |
| Vector Store | ChromaDB (Persistent, Local) |
| Memory | LangChain `RunnableWithMessageHistory` |
| Document Loader | `PyPDFLoader` |
| Framework | LangChain + LangChain Classic |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/conversational-rag-pdf-chatbot.git
cd conversational-rag-pdf-chatbot
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get your free API keys

| Service | Link | Cost |
|---|---|---|
| Groq API Key | [console.groq.com](https://console.groq.com) | Free |
| HuggingFace Token | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | Free |

### 5. Create `.env` file in the project root
```env
GROQ_API_KEY=gsk_your_groq_key_here
HF_TOKEN=hf_your_huggingface_token_here
```

### 6. Run the app
```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## 🖥️ How to Use

1. Open the app in your browser
2. Upload one or more PDF files using the file uploader
3. Wait for the documents to be processed
4. Type your question in the input box
5. Ask follow-up questions — the app remembers context automatically
6. Expand **Chat History** to see the full conversation

---

## 📁 Project Structure

```
conversational-rag-pdf-chatbot/
├── app.py              # Main Streamlit application
├── .env                # API keys (never commit this!)
├── .gitignore          # Ignores venv, chroma_db, .env
├── requirements.txt    # Python dependencies
├── chroma_db/          # Auto-created local vector store
└── README.md           # This file
```

---

## 🔧 Requirements

```
streamlit
langchain
langchain-classic
langchain-core
langchain-community
langchain-chroma
langchain-groq
langchain-huggingface
langchain-text-splitters
chromadb
pypdf
python-dotenv
sentence-transformers
```

---

## 🏢 Use Cases

- **Legal** — Query contracts, agreements, and legal briefs
- **Finance** — Extract insights from earnings reports and filings
- **Healthcare** — Search clinical papers and medical documentation
- **Education** — Study assistant for textbooks and lecture notes
- **Enterprise** — Internal knowledge base for policies and SOPs

---

## 🚀 Future Improvements

- [ ] Multi-user authentication
- [ ] Persistent memory across sessions (PostgreSQL/Redis)
- [ ] Source citation with page numbers
- [ ] Support for Word, Excel, and web URLs
- [ ] Streaming LLM responses
- [ ] Docker + cloud deployment
- [ ] RAG evaluation pipeline (RAGAS)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

> Built with ❤️ using Streamlit, LangChain, Groq, and ChromaDB
