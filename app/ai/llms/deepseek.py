from langchain_deepseek import ChatDeepSeek
from langchain_core.callbacks import BaseCallbackHandler
from app.config import DeepSeekConfig as config

def build_deepseek_llm(streaming: bool,
                     handlers: [BaseCallbackHandler]):
    """
        Build Deepseek Model
        Args:
            streaming(bool): Enable streaming
            handlers(BaseCallbackHandler): Callback Handlers
        """
    return ChatDeepSeek(
        streaming=streaming,
        model=config.MODEL_NAME,
        callbacks=handlers,
    )