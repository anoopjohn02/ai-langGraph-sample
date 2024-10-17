"""
OpenAI Module
"""
import tiktoken
from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.config import OpenaiConfig as config

OPENAI_MODEL_NAME = config.model
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
embeddings = OpenAIEmbeddings(model = OPENAI_EMBEDDING_MODEL)
encoding = tiktoken.encoding_for_model(OPENAI_EMBEDDING_MODEL)

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
        model_name=OPENAI_MODEL_NAME,
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
