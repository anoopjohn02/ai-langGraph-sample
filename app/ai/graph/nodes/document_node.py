from typing import Any, Dict

from app.data.vector import build_retriever
from ..state import GraphState


def retrieve_document_node(state: GraphState) -> Dict[str, Any]:
    """
    Vector retriever node
    """
    query = state["question"]
    retriever = build_retriever()
    documents = retriever.get_relevant_documents(query)
    return {"documents": documents, "question": query}