from app.ai.llms import EMBEDDING_MODEL, MODEL_NAME
from .token_handler import TokenAsyncHandler
from ..llms import calculate_tokens
from ...models.chat import ChatArgs
from ...models.token import TransactionalTokens


def build_token_handler(chat_args: ChatArgs):
    token = TransactionalTokens(query=chat_args.query,
                                transaction_id=chat_args.transaction_id,
                                conversation_id=chat_args.conversation_id,
                                model=MODEL_NAME,
                                embedding_model=EMBEDDING_MODEL)
    return TokenAsyncHandler(token, calculate_tokens)