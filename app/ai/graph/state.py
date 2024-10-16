from typing import List, TypedDict, Any


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        user_id: user id
        generation: LLM generation
        documents: list of documents
    """

    question: str
    user_id: str
    generation: str
    documents: List[Any]
