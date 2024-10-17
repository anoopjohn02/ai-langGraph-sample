from uuid import UUID
from typing import List, TypedDict, Any


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        user_id: user id
        conversation_id: conversation id
        transaction_id: transaction id
        question: question
        generation: LLM generation
        documents: list of documents
    """
    user_id: UUID
    conversation_id: UUID
    transaction_id: UUID
    question: str
    generation: str
    documents: List[str]
