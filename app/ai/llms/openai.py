"""
OpenAI Module
"""
import tiktoken
from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.config import OpenaiConfig as config
from app.models.chat import ChatArgs

OPENAI_MODEL_NAME = config.model
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
embeddings = OpenAIEmbeddings(model = OPENAI_EMBEDDING_MODEL)
encoding = tiktoken.encoding_for_model(OPENAI_EMBEDDING_MODEL)

def build_openai_llm(chat_args: ChatArgs, handlers: [BaseCallbackHandler]):
    """
    Build OpenAI Model
    Args:
        chat_args(ChatArgs): Arguments needed for building OpenAI model
        handlers(BaseCallbackHandler): Callback Handlers
    """
    return ChatOpenAI(
        streaming=chat_args.streaming,
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
