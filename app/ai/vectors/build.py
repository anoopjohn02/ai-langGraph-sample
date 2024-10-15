"""
Build module
"""
from .chroma import build_chroma_retriever, get_chroma

def build_retriever():
    """
    Method to build retriever
    """
    return build_chroma_retriever()

def build_vector_store():
    """
    Method to build store
    """
    return get_chroma()
