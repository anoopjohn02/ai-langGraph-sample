"""
Chat Module
"""

import logging

from app.ai.graph.graph import app
from app.models.chat import ChatArgs


def get_response(chat_args: ChatArgs):
    logging.info("Question %s", chat_args.query)
    result = app.invoke(input={
        "question": chat_args.query,
        "user_id": chat_args.user_id,
        "conversation_id": chat_args.conversation_id,
        "transaction_id": chat_args.transaction_id
    })
    print(result)
