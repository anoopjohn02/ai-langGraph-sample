"""
Memory build module
"""
from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationTokenBufferMemory
)

from app.models.chat import ChatArgs
from .histories import SqlMessageHistory


def build_memory(chat_args: ChatArgs):
    """
    Build Conversation Buffer Memory
    Args:
        chat_args(ChatArgs): Arguments needed for building Conversation Buffer Memory
    """
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(
            conversation_id = chat_args.conversation_id,
            transaction_id = chat_args.transaction_id
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="output"
    )

def build_window_memory(chat_args):
    """
    Build Conversation Buffer Window Memory
    Args:
        chat_args(ChatArgs): Arguments needed for building Conversation Buffer Window Memory
    """
    return ConversationBufferWindowMemory(
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer",
        k=2
    )

def build_token_memory(chat_args):
    """
    Build Conversation Token Memory
    Args:
        chat_args(ChatArgs): Arguments needed for building Conversation Token Memory
    """
    return ConversationTokenBufferMemory(
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer",
        max_token_limit=1000
    )
