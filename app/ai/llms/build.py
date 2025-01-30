"""
LLM Build Module
"""
from .openai import (build_openai_llm,
                     build_openai_condense_llm,
                     embeddings)
from .ollama import build_ollama_llm
from ..graph.state import GraphState
from ..handlers.build import build_token_handler

def build_llm(state: GraphState, streaming: bool):
    """
    Build LLM Function
    """
    token_handler = build_token_handler(state)
    handlers = [token_handler]
    return build_openai_llm(streaming, handlers)

def build_local_llm(state: GraphState, streaming: bool):
    """
    Build local LLM Function
    """
    token_handler = build_token_handler(state)
    handlers = [token_handler]
    return build_ollama_llm(streaming, handlers)

def build_condense_llm():
    """
    Build condense LLM
    """
    return build_openai_condense_llm()

def build_embeddings():
    """
    Build embeddings
    """
    return embeddings
