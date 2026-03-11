# DocuMind AI 🧠📄

**An Intelligent Multi-Document Retrieval-Augmented Generation (RAG) System**

DocuMind AI is an AI-powered document intelligence platform that allows users to upload multiple PDF documents and query them using natural language. The system uses Retrieval-Augmented Generation (RAG) to combine semantic search with large language models to provide accurate, context-grounded answers with source citations.

---

## 🚀 Features

* 📄 **Multi-Document Upload**
  Upload and process multiple PDFs into a unified knowledge base.

* 🔍 **Semantic Search with Vector Embeddings**
  Documents are chunked and embedded using sentence-transformers to enable similarity-based retrieval.

* 🧠 **RAG-based Question Answering**
  Combines retrieved document context with a Large Language Model to generate accurate responses.

* 📚 **Source Citations**
  Every answer includes references to the document and page number used.

* ⚡ **FastAPI Backend API**
  Production-style REST API for document ingestion and querying.

* 💾 **Persistent Vector Database**
  Uses ChromaDB to store embeddings and maintain a persistent knowledge base.

* 🧩 **Modular Architecture**
  Clean separation between ingestion, retrieval, embedding, and generation layers.

---

## 🏗 System Architecture

User Query
↓
FastAPI API Layer
↓
Retriever (Chroma Vector DB)
↓
Relevant Document Chunks
↓
LLM (Groq Llama-3 Model)
↓
Answer + Source Citations

---

## ⚙️ Tech Stack

**Backend**

* Python
* FastAPI
* LangChain
* Uvicorn

**AI / ML**

* Sentence Transformers
* Chroma Vector Database
* Groq LLM (Llama-3)

**Data Processing**

* PyPDFLoader
* Recursive Text Chunking

---

## 📂 Project Structure

```
documind-ai
│
├── backend
│   ├── main.py              # FastAPI application
│   ├── document_loader.py  # PDF ingestion
│   ├── text_splitter.py    # Document chunking
│   ├── embedding.py        # Embedding generation
│   ├── vector_store.py     # Chroma vector database
│   ├── retriever.py        # Retrieval layer
│   ├── rag_pipeline.py     # RAG orchestration
│   └── llm.py              # LLM integration
│
├── uploads                 # Uploaded PDFs
├── vector_db               # Persistent vector database
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

### 1. Document Ingestion

PDF documents are uploaded through the `/upload` endpoint.

The system:

* Extracts text from PDFs
* Splits text into chunks
* Generates embeddings
* Stores them in the vector database

### 2. Retrieval

When a user asks a question:

* The query is embedded
* Similar document chunks are retrieved from ChromaDB

### 3. Generation

The retrieved context is passed to the LLM which generates a grounded answer.

---

## 📡 API Endpoints

### Health Check

```
GET /
```

Response

```
{
  "message": "DocuMind AI API running"
}
```

---

### Upload Document

```
POST /upload
```

Uploads a PDF and adds it to the knowledge base.

---

### Ask Question

```
POST /ask
```

Example request:

```
{
  "question": "What does the document say about artificial intelligence?"
}
```

Example response:

```
{
  "answer": "Artificial intelligence is transforming industries...",
  "sources": [
    {
      "file": "sample.pdf",
      "page": 1
    }
  ]
}
```

---

## 🛠 Installation

Clone the repository:

```
git clone https://github.com/yourusername/documind-ai.git
cd documind-ai
```

Create virtual environment:

```
python -m venv venv
```

Activate it:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Set your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶ Running the Server

Start the FastAPI server:

```
uvicorn backend.main:app --reload
```

Open the API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Future Improvements

* Hybrid retrieval (semantic + keyword search)
* Query rewriting for improved search accuracy
* Chat-style UI interface
* Answer confidence scoring
* Streaming responses
* Knowledge graph extraction

---

## 🎯 Use Cases

* Enterprise document search
* Research paper exploration
* Internal company knowledge bases
* Legal and compliance document analysis
* AI-powered document assistants

---

## 👨‍💻 Author

**Arnav Bhende**

Built as a practical exploration of modern Retrieval-Augmented Generation systems and document intelligence architectures.

---

## 📜 License

MIT License
