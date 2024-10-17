"""
Costs per transaction
"""
import uuid
from datetime import datetime, timedelta
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.user import User, TokenUser


class Document(BaseModel):
    """
    Document Embedding Dto
    """
    id: Optional[UUID] = None
    file_name: str
    num_chunks: int
    num_tokens: int
    processed_date: datetime
    last_modified: datetime

class Embedding(BaseModel):
    """
    Document Embedding Dto
    """
    id: Optional[UUID] = None
    embedding_model: str
    chunk_size: int
    chunk_overlap: int
    token_encoding_model: str
    docs: Optional[List[Document]] = []

class Message(BaseModel):
    """
    Message Dto
    """
    type: str
    content: str

class TotalTokenUsage(BaseModel):
    model: str
    tokens: int = 0
    cost: float = 0
    execution_time: timedelta = 0
    created_on: datetime
    user: Optional[TokenUser] = None
    messages: Optional[List[Message]] = []

class TokenUsage(BaseModel):
    """
    Token Usage Dto
    """
    transaction_id: Optional[UUID] = None
    llm_model: str
    embedding_model: str
    start_time: datetime
    end_time: datetime
    prompt_tokens: int = 0
    output_tokens: int = 0
    prompt_cost: float = 0
    output_cost: float = 0
    embedding_cost: float = 0
    created_on: datetime
    user: Optional[User] = None
    messages: Optional[List[Message]] = []

class TransactionalTokens:
    """
    Token information per transaction
    """
    query: str
    model: str
    embedding_model: str
    start_time: datetime
    end_time: datetime
    transaction_id: uuid
    conversation_id: uuid
    prompt_tokens: int = 0
    output_tokens: int = 0
    successful_requests: int = 0

    def __init__( self, query, conversation_id, transaction_id, model, embedding_model):
        self.query = query
        self.transaction_id = uuid.UUID(transaction_id).hex
        self.conversation_id = uuid.UUID(conversation_id).hex
        self.model = model
        self.embedding_model = embedding_model

    def sum_prompt_tokens( self, tokens: int ):
        """
        Add prompt count to existing count
        """
        self.prompt_tokens = self.prompt_tokens + tokens

    def sum_output_tokens( self, tokens: int ):
        """
        Add output count to existing count
        """
        self.output_tokens = self.output_tokens + tokens

    def sum_successful_requests( self, requests: int ):
        """
        Add request count to existing count
        """
        self.successful_requests = self.successful_requests + requests
