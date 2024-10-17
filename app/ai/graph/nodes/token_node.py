
import logging
import uuid
from typing import Any, Dict, List

from app.models.token import TotalTokenUsage
from app.models.user import TokenUser
from app.services.token_usage import get_user_message_token_usage
from ..state import GraphState


def token_usage_node(state: GraphState) -> Dict[str, Any]:
    user_id = state["user_id"]
    query = state["question"]
    logging.info("token_usage_query: User with id %s", user_id)
    documents: List[TotalTokenUsage] = []
    for token in get_user_message_token_usage(uuid.UUID(user_id).hex):
        documents.append(TotalTokenUsage(
            model=token.llm_model, tokens=token.prompt_tokens + token.output_tokens,
            cost=token.prompt_cost + token.output_cost + token.embedding_cost,
            execution_time=(token.end_time - token.start_time),
            created_on=token.created_on, user=TokenUser(**token.user.__dict__),
            messages=token.messages
        ))
    return {"documents": documents, "question": query}