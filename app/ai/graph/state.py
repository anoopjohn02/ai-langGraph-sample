from uuid import UUID
from typing import List, TypedDict, Any


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        user_id: user id
        conversation_id: conversation id
        transaction_id: transaction id
        question: question from user
        answer: LLM generated answer
        documents: list of documents
        documents_json: document in json format
    """
    user_id: UUID
    conversation_id: UUID
    transaction_id: UUID
    question: str
    answer: str
    documents: List[str]
    documents_json: str
