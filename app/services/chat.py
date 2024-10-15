"""
Chat service module
"""
import uuid

from app.ai import build_agent
from app.models.chat import ChatArgs, Request
from app.models.user import LoggedInUser
from .conversation import get_default_user_conversation, create_new_user_conversation


class ChatService:
    """
    Chat service class
    """

    def create_agent(self, request: Request, user: LoggedInUser):
        """
        Create agent
        """
        if request.new_chat:
            conversation_id = create_new_user_conversation(user.id)
        else:
            conversation_id = get_default_user_conversation(user.id)
        chat_args = ChatArgs(user.id, request.question, conversation_id, uuid.uuid1(), True)
        return build_agent(chat_args)