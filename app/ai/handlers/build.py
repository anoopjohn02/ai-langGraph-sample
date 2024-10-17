from .token_handler import TokenAsyncHandler
from ..graph.state import GraphState
from ..llms import EMBEDDING_MODEL, MODEL_NAME,calculate_tokens
from ...models.token import TransactionalTokens


def build_token_handler(state: GraphState):
    token = TransactionalTokens(query=state["question"],
                                transaction_id=state["transaction_id"],
                                conversation_id=state["conversation_id"],
                                model=MODEL_NAME,
                                embedding_model=EMBEDDING_MODEL)
    return TokenAsyncHandler(token, calculate_tokens)