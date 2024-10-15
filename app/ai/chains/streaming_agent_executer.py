"""
Streaming Conversational Retrieval Chain
"""
from langchain.agents import AgentExecutor

from app.ai.chains.stream import Streamable


class StreamingAgentExecutor(Streamable, AgentExecutor):
    """
    Custom class for streaming
    """
    pass