
from langchain_ollama import ChatOllama
from langchain_core.callbacks import BaseCallbackHandler
from app.config import OllamaConfig as config

def build_ollama_llm(streaming: bool,
                     handlers: [BaseCallbackHandler]):
    """
    Build Ollama Model
    Args:
        streaming(bool): Enable streaming
        handlers(BaseCallbackHandler): Callback Handlers
    """
    return ChatOllama(
        streaming=streaming,
        model=config.MODEL_NAME,
        callbacks=handlers,
    )