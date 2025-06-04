from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from config import OPENAI_API_KEY, INDEX_PATH, LLM_MODEL

def get_rag_chain():
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = FAISS.load_local(INDEX_PATH, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=LLM_MODEL, temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

def query_rag(prompt):
    rag = get_rag_chain()
    return rag.run(prompt)
