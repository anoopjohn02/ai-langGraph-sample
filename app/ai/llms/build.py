"""
LLM Build Module
"""
from .openai import (build_openai_llm,
                     build_openai_condense_llm,
                     embeddings)
from .ollama import build_ollama_llm
from .deepseek import build_deepseek_llm
from ..graph.state import GraphState
from ..handlers.build import build_token_handler
from app.config.load_config import App

def build_llm(state: GraphState, streaming: bool):
    """
    Build LLM Function
    """
    token_handler = build_token_handler(state)
    handlers = [token_handler]
    if App.MODEL_TYPE == 'openai':
        return build_openai_llm(streaming, handlers)
    elif App.MODEL_TYPE == 'ollama':
        return build_ollama_llm(streaming, handlers)
    elif App.MODEL_TYPE == 'deepseek':
        return build_deepseek_llm(streaming, handlers)

def default_llm(state: GraphState, streaming: bool):
    """
    Build LLM for Router
    """
    token_handler = build_token_handler(state)
    handlers = [token_handler]
    return build_openai_llm(streaming, handlers)

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
