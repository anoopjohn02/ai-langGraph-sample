"""
Chat service module
"""
import uuid

from app.ai import get_response
from app.models.chat import ChatArgs, Request
from app.models.user import LoggedInUser
from .conversation import get_default_user_conversation, create_new_user_conversation


class ChatService:
    """
    Chat service class
    """

    def answer(self, request: Request, user: LoggedInUser):
        """
        Create agent
        """
        if request.new_chat:
            conversation_id = create_new_user_conversation(user.id)
        else:
            conversation_id = get_default_user_conversation(user.id)
        chat_args = ChatArgs(user.id, request.question, conversation_id, uuid.uuid1(), True)
        get_response(chat_args)
        return None

    async def fake_data(self):
        for i in range(10):
            yield f"some fake data {i} <br>"