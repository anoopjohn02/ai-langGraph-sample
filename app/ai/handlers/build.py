from .token_handler import TokenAsyncHandler
from ..graph.state import GraphState
from ..llms.tokens import calculate_tokens
from ...models.token import TransactionalTokens
from app.config import OpenaiConfig as config

def build_token_handler(state: GraphState):
    token = TransactionalTokens(query=state["question"],
                                transaction_id=state["transaction_id"],
                                conversation_id=state["conversation_id"],
                                model=config.MODEL_NAME,
                                embedding_model=config.EMBEDDING_MODEL)
    return TokenAsyncHandler(token, calculate_tokens)