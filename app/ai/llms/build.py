"""
LLM Build Module
"""
from .openai import (build_openai_llm,
                     build_openai_condense_llm,
                     calculate_openai_tokens,
                     embeddings)
from ..graph.state import GraphState
from ..handlers import build_token_handler


def build_llm(state: GraphState, streaming: bool):
    """
    Build LLM Function
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

def calculate_tokens(texts):
    """
    Calculate tokens in a text
    """
    return calculate_openai_tokens(texts)
