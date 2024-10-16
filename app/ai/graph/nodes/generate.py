from typing import Any, Dict
from langchain.prompts import (PromptTemplate, ChatPromptTemplate,
                               HumanMessagePromptTemplate, MessagesPlaceholder)
from langchain.schema import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from app.config import CUSTOM_PROMPT
from ..state import GraphState
from ...llms import build_llm

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=CUSTOM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

def generate_output_node(state: GraphState) -> Dict[str, Any]:

    question = state["question"]
    documents = state["documents"]

    llm = build_llm(state, True)
    generation_chain = prompt | llm | StrOutputParser()
    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}