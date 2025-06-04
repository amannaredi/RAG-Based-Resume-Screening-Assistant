import os
import faiss
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from config import OPENAI_API_KEY, INDEX_PATH

def load_resumes(folder_path="resumes/"):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, filename))
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
            documents.append({"text": text, "metadata": {"filename": filename}})
    return documents

def build_index():
    resumes = load_resumes()
    texts = [r["text"] for r in resumes]
    metadata = [r["metadata"] for r in resumes]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents(texts, metadatas=metadata)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = FAISS.from_documents(chunks, embeddings)

    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    db.save_local(INDEX_PATH)
    print("✅ FAISS index built and saved.")

if __name__ == "__main__":
    build_index()
