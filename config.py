import os

# Set your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "your-openai-api-key"

# Embedding and LLM models
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-3.5-turbo"

# FAISS Index Path
INDEX_PATH = "faiss_index/resume_index"
