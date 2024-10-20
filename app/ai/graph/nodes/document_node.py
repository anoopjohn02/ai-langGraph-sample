import logging
from typing import Any, Dict

from app.data.vector import build_retriever
from ..state import GraphState


def retrieve_document_node(state: GraphState) -> Dict[str, Any]:
    """
    Vector retriever node
    """
    question = state.get("refined_question", state["question"])
    logging.info("Vector question: %s", question)
    retriever = build_retriever()
    documents = retriever.invoke(question)
    chunks = [doc.page_content for doc in documents]
    return {"documents": chunks}