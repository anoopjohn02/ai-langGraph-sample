from typing import Any, Dict

from ..state import GraphState
from app.data.vector import build_retriever


def retrieve_node(state: GraphState) -> Dict[str, Any]:
    """
    Vector retriever node
    """
    query = state["question"]
    retriever = build_retriever()
    documents = retriever.get_relevant_documents(query)
    return {"documents": documents, "question": query}