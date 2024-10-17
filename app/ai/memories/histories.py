"""
The chat history module
"""
import logging
import uuid

from langchain.schema import BaseChatMessageHistory

from app.services.conversation import (
    add_message_to_conversation,
    get_messages_by_conversation_id
)


class SqlMessageHistory(BaseChatMessageHistory):
    """
    SQL Message History Module
    """
    conversation_id: uuid
    transaction_id: uuid
    def __init__(self, conversation_id, transaction_id) -> None:
        self.conversation_id = uuid.UUID(conversation_id).hex
        self.transaction_id = uuid.UUID(transaction_id).hex
        super().__init__()

    @property
    def messages(self):
        """
        Get Messages
        """
        logging.debug("Fetching from memory")
        return get_messages_by_conversation_id(self.conversation_id)
    def add_message(self, message):
        """
        Save message
        """
        logging.debug("Adding message to history.")
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content,
            transaction_id=self.transaction_id
        )
    def clear(self):
        """
        Delete all messages
        """
        logging.info("Clearing the messages NOT implemented")
