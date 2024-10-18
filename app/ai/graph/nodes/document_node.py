from typing import Any, Dict

from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

from app.config import CUSTOM_PROMPT
from app.data.vector import build_retriever
from ..state import GraphState

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=CUSTOM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        MessagesPlaceholder(variable_name="context"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)
def retrieve_document_node(state: GraphState) -> Dict[str, Any]:
    """
    Vector retriever node
    """
    question = state["question"]
    retriever = build_retriever()
    documents = retriever.invoke(question)
    chunks = [doc.page_content for doc in documents]
    return {"documents": chunks}