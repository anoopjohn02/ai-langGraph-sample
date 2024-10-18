"""
OpenAI Module
"""
import tiktoken
from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.config import OpenaiConfig as config

embeddings = OpenAIEmbeddings(model = config.EMBEDDING_MODEL)
encoding = tiktoken.encoding_for_model(config.EMBEDDING_MODEL)

def build_openai_llm(streaming: bool,
                     handlers: [BaseCallbackHandler]):
    """
    Build OpenAI Model
    Args:
        streaming(bool): Enable streaming
        handlers(BaseCallbackHandler): Callback Handlers
    """
    return ChatOpenAI(
        streaming=streaming,
        model_name=config.MODEL_NAME,
        callbacks=handlers,
    )

def build_openai_condense_llm():
    """
    Build condense OpenAI model
    """
    return ChatOpenAI(streaming=False)

def calculate_openai_tokens(texts):
    """
    Calculate tokens in a text
    """
    total_tokens = sum(len(encoding.encode(text))
                       for text in texts)
    return total_tokens
