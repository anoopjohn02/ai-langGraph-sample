from typing import Any, Dict

from langchain.prompts import (ChatPromptTemplate,
                               HumanMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import SystemMessage
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

from app.config import CUSTOM_PROMPT
from app.services.conversation import get_conversation_summary
from ..state import GraphState
from ...llms import build_llm

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=CUSTOM_PROMPT),
        MessagesPlaceholder(variable_name="context"),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

async def generate_output_node(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    conversation_id = state["conversation_id"]
    summary = get_conversation_summary(conversation_id)
    documents = state.get("documents", [])

    llm = build_llm(state, True)
    chain = prompt | llm | StrOutputParser()
    answer = await chain.ainvoke({"context": documents, "question": question, "chat_history": [summary]})

    messages = [HumanMessage(content=question), AIMessage(content=answer)]
    return {"question": question, "answer": answer, "conv_summary": summary, "messages": messages}