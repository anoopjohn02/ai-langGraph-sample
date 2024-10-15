
import logging
import uuid
from typing import List

from langchain_core.tools import Tool

from app.models.token import TotalTokenUsage
from app.models.user import TokenUser
from app.services.token_usage import get_user_message_token_usage


def token_usage_tool(user_id: str, *args) -> List[TotalTokenUsage]:
    logging.info("token_usage_query: User with id %s", user_id)
    totals: List[TotalTokenUsage] = []
    for token in get_user_message_token_usage(uuid.UUID(user_id).hex):
        totals.append(TotalTokenUsage(
            model=token.llm_model, tokens=token.prompt_tokens + token.output_tokens,
            cost=token.prompt_cost + token.output_cost + token.embedding_cost,
            execution_time=(token.end_time - token.start_time),
            created_on=token.created_on, user=TokenUser(**token.user.__dict__),
            messages=token.messages
        ))
    return totals

def define_user_token_usage_tool(user_id: str):
    def token_usage_tool_wrapper(*args) -> List[TotalTokenUsage]:
        logging.info("Given: %s", args)
        return token_usage_tool(user_id, args)

    return Tool.from_function(
        name="token_usage_tool",
        description="Use this tool when query contains token, cost, model, and execution time. "
                    "This tool provides the list of token usages including "
                    "- number of tokens used so far"
                    "- cost of each tokens"
                    "- first name and last name of user who used the toke"
                    "- execution time"
                    "- messages corresponding to each token"
                    "- llm model used for token",
        func=token_usage_tool_wrapper
    )