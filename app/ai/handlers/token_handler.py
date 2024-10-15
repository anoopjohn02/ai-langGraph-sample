"""
Token handler module
"""
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from langchain.callbacks.base import AsyncCallbackHandler
from langchain.schema import LLMResult
from langchain_core.messages import BaseMessage

from app.models.token import TransactionalTokens
from app.services.token_usage import save_message_token_usage


class TokenAsyncHandler(AsyncCallbackHandler):
    """
    Token Handler class
    """
    txn_token: TransactionalTokens
    calculate_tokens: any
    def __init__(self, txn_token, calculate_tokens):
        self.txn_token = txn_token
        self.calculate_tokens = calculate_tokens

    async def on_llm_start( self, serialized: Dict[str, Any],
                           prompts: List[str], **kwargs: Any) -> None:
        logging.info("LLM Started")
        if self.txn_token == None: return
        if self.calculate_tokens:
            for prompt in prompts:
                self.txn_token.sum_prompt_tokens(self.calculate_tokens(prompt))
        self.txn_token.start_time = datetime.utcnow()

    async def on_chat_model_start(self, serialized: Dict[str, Any],
                                  messages: List[List[BaseMessage]], *,
                                  run_id: UUID, parent_run_id: Optional[UUID] = None,
                                  tags: Optional[List[str]] = None,
                                  metadata: Optional[Dict[str, Any]] = None,
                                  **kwargs: Any,) -> Any:
        logging.info("Chat Model Started")
        if self.calculate_tokens:
            for message_list in messages:
                for message in message_list:
                    logging.info(f"Prompt sent to LLM: {message.content}")
                    self.txn_token.sum_prompt_tokens(self.calculate_tokens(message.content))
        self.txn_token.start_time = datetime.utcnow()

    async def on_llm_new_token(self, token: str, **kwargs) -> None:
        if self.calculate_tokens:
            self.txn_token.sum_output_tokens(self.calculate_tokens(token))

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        self.txn_token.sum_successful_requests( 1 )
        logging.info("LLM Ended")
        self.txn_token.end_time = datetime.utcnow()
        save_message_token_usage(self.txn_token)
