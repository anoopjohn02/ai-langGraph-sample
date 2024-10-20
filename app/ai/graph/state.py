from typing import List, TypedDict, Annotated
from uuid import UUID

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


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
    """
    user_id: UUID
    conversation_id: UUID
    transaction_id: UUID
    question: str
    refined_question: str
    answer: str
    documents: List[str]
    conv_summary: str
    messages: List[BaseMessage]
    stream_messages: Annotated[list, add_messages]
