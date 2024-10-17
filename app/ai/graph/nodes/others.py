
from typing import Any, Dict
from langchain_core.messages import SystemMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

from app.config import CUSTOM_PROMPT
from app.data.vector import build_retriever

from ..state import GraphState
from ...chains import StreamingConversationalRetrievalChain
from ...llms import build_llm
from ...memories import build_memory

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=CUSTOM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        MessagesPlaceholder(variable_name="context"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

def other_node(state: GraphState) -> Dict[str, Any]:
    return {"documents": [], "documents_json": ""}