"""
Message Token Usage Module
"""
import logging
import uuid
from typing import List

from app.config.constants import MODEL_COSTS
from app.data.sql.entities import MessageTokenUsage
from app.data.sql.repo import MessageTokenUsageRepo, DocumentEmbeddingRepo
from app.models.token import (TransactionalTokens,
                              TokenUsage,
                              Message,
                              Embedding,
                              Document)
from app.models.user import User
from .conversation import get_messages_by_transaction_id

messageTokenRepo = MessageTokenUsageRepo()
embeddingRepo = DocumentEmbeddingRepo()

def save_message_token_usage(txn_token: TransactionalTokens):
    """
    Method to save message token usage
    """
    logging.debug("Saving Transaction: txn_id=%s", txn_token.transaction_id)
    logging.debug("Token usages: prompt_tokens=%s, output_tokens=%s",
                  txn_token.prompt_tokens, txn_token.output_tokens)
    token_usage = MessageTokenUsage()
    token_usage.id = uuid.uuid1()
    token_usage.transaction_id = txn_token.transaction_id
    token_usage.conversation_id = txn_token.conversation_id
    token_usage.llm_model = txn_token.model
    token_usage.embedding_model = txn_token.embedding_model
    token_usage.start_time = txn_token.start_time
    token_usage.end_time = txn_token.end_time
    token_usage.prompt_tokens = txn_token.prompt_tokens
    token_usage.output_tokens = txn_token.output_tokens
    if isinstance(MODEL_COSTS[txn_token.model], dict):
        prompt_cost = (txn_token.prompt_tokens / 1000) * MODEL_COSTS[txn_token.model]['input']
        output_cost = (txn_token.output_tokens / 1000) * MODEL_COSTS[txn_token.model]['output']
    else:
        prompt_cost = (txn_token.prompt_tokens / 1000) * MODEL_COSTS[txn_token.model]
        output_cost = (txn_token.output_tokens / 1000) * MODEL_COSTS[txn_token.model]
    token_usage.prompt_cost = prompt_cost
    token_usage.output_cost = output_cost
    embedding_tokens = len(txn_token.query) // 4
    embedding_cost = (embedding_tokens / 1000) * MODEL_COSTS[txn_token.embedding_model]
    token_usage.embedding_cost = format(embedding_cost, '.9f')
    logging.debug("Token costs: prompt_cost=%s, output_cost=%s, embedding_cost=%s",
                  prompt_cost, output_cost, token_usage.embedding_cost)
    messageTokenRepo.save_usage(token_usage)

def get_message_token_usage() -> List[TokenUsage]:
    """
    Method to get all message token usages
    """
    usages:List[TokenUsage] = []
    tokens = messageTokenRepo.get_all_message_usages()
    for token in tokens:
        dto = TokenUsage(**token.__dict__)
        dto.llm_model = token.llm_model
        messages = get_messages_by_transaction_id(token.transaction_id)
        dto.messages = [Message(**message.__dict__) for message in messages]
        dto.user = User(id=token.conversation_history.user_id, first_name="Anoop", last_name="John")
        usages.append(dto)
    return usages

def get_document_embeddings() -> List[Embedding]:
    """
    Method to get all embeddings
    """
    embeddings:List[Embedding] = []
    entities = embeddingRepo.get_all()
    for entity in entities:
        dto = Embedding(**entity.__dict__)
        dto.docs = [Document(**doc.__dict__) for doc in entity.files]
        embeddings.append(dto)
    return embeddings

def get_user_message_token_usage(user_id: uuid) -> List[TokenUsage]:
    """
    Method to get user message token usages
    """
    usages: List[TokenUsage] = []
    tokens = messageTokenRepo.get_user_message_usages(user_id)
    for token in tokens:
        dto = TokenUsage(**token.__dict__)
        dto.llm_model = token.llm_model
        messages = get_messages_by_transaction_id(token.transaction_id)
        dto.messages = [Message(**message.__dict__) for message in messages]
        dto.user = User(id=token.conversation_history.user_id)
        usages.append(dto)
    return usages