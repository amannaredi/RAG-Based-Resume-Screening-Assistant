# 🔍 RAG-Based Resume Screening Assistant

A Retrieval-Augmented Generation (RAG) application that lets recruiters ask natural language questions (e.g., "Find resumes with Flask and AWS experience") and retrieves the most relevant candidates using embeddings and GPT-powered reasoning.

## 🚀 Features

- 🔎 Semantic search over resumes using OpenAI embeddings + FAISS
- 🤖 GPT-4 (or GPT-3.5-turbo) powered natural language answering
- 🧠 Retrieval-Augmented Generation (RAG) pipeline using LangChain
- 📄 PDF resume ingestion, chunking, and indexing
- 🌐 Flask backend API for easy integration

## 🛠️ Tech Stack

- Python
- Flask
- OpenAI (Embeddings + LLM)
- FAISS (Vector Database)
- LangChain
- PyPDF2

## 📁 Project Structure

```
rag-resume-assistant/
├── app.py                 
├── config.py              
├── ingest.py              
├── rag_pipeline.py        
├── requirements.txt
├── resumes/               # Folder containing input resumes (PDFs)
└── faiss_index/           # Saved FAISS vector index
```

## 📦 Setup Instructions

1. **Install dependencies**  
```bash
pip install -r requirements.txt
```

2. **Set your OpenAI API Key**  
```bash
export OPENAI_API_KEY=your-api-key
```

3. **Ingest resumes into FAISS index**  
```bash
python ingest.py
```

4. **Start the Flask API**  
```bash
python app.py
```

5. **Query Example**
```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "Who has experience with Flask and AWS?"}'
```

## ✅ Example Use Cases

- AI-powered candidate search by skills, tools, or experience
- Automated resume summarization and filtering
- Semantic job-role matching in recruitment pipelines

## 📄 License

MIT License
