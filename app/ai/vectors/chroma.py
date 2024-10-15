"""
The chroma module
"""
from langchain_chroma import Chroma

from app.ai.llms import build_embeddings
from app.config import ChromaConfig as config

db = Chroma(
    persist_directory=config.dir,
    embedding_function = build_embeddings()
)

def build_chroma_retriever():
    """
    Method to build chroma retriever
    """
    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )
    return retriever

def get_chroma():
    """
    Get chroma DB
    """
    return db
