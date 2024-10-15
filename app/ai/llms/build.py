"""
LLM Build Module
"""
from langchain_core.callbacks import BaseCallbackHandler

from app.models.chat import ChatArgs
from .openai import (build_openai_llm,
                     build_openai_condense_llm,
                     calculate_openai_tokens,
                     embeddings)


def build_llm(chat_args: ChatArgs, handlers: [BaseCallbackHandler]):
    """
    Build LLM Function
    """
    return build_openai_llm(chat_args, handlers)

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
