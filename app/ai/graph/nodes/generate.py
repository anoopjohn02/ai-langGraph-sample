from typing import Any, Dict

from langchain.prompts import (ChatPromptTemplate,
                               HumanMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import SystemMessage
from langchain_core.output_parsers import StrOutputParser

from app.config import CUSTOM_PROMPT_TEMPLATE
from ..state import GraphState
from ...llms import build_llm
from ...memories import build_memory

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=CUSTOM_PROMPT_TEMPLATE),
        MessagesPlaceholder(variable_name="context"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

def generate_output_node(state: GraphState) -> Dict[str, Any]:

    question = state["question"]
    documents = state["documents"]

    llm = build_llm(state, True)
    memory = build_memory(state)
    generation_chain = prompt | llm | StrOutputParser()
    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}