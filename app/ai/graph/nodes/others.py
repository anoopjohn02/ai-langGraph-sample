
from typing import Any, Dict

from ..state import GraphState


def other_node(state: GraphState) -> Dict[str, Any]:
    query = state["question"]
    return {"documents": [], "question": query}