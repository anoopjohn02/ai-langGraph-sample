"""
Streaming Conversational Retrieval Chain
"""
from langchain.chains import ConversationalRetrievalChain

from app.ai.chains.stream import Streamable


class StreamingConversationalRetrievalChain(Streamable, ConversationalRetrievalChain):
    """
    Custom class for streaming
    """
    pass
