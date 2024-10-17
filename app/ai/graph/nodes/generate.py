from typing import Any, Dict

from langchain.prompts import (ChatPromptTemplate,
                               HumanMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import SystemMessage
from langchain_core.output_parsers import StrOutputParser

from app.config import CUSTOM_PROMPT
from ..state import GraphState
from ...llms import build_llm
from ...memories import build_memory

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=CUSTOM_PROMPT),
        MessagesPlaceholder(variable_name="context"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

def generate_output_node(state: GraphState) -> Dict[str, Any]:

    question = state["question"]
    documents = state["documents"]
    if len(documents) > 0:
        context = documents
    else:
        context = state["documents_json"]

    llm = build_llm(state, True)
    memory = build_memory(state)
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": question})
    return {"question": question, "answer": answer}