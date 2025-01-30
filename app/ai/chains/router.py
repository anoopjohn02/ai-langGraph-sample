from typing import Literal

from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field

from app.ai.graph.state import GraphState
from app.ai.llms import default_llm


class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "tokens", "devices", "others"] = Field(
        ...,
        description="Given a user question choose to route it to vectorstore or tokens or devices.",
    )

def build_llm_router(state: GraphState):
    llm = default_llm(state, False)
    structured_llm_router = llm.with_structured_output(RouteQuery)
    system = """You are an expert at routing a user question to a vectorstore or tokens or devices.
    The vectorstore contains documents related to spices. Use the vectorstore for the questions on these topics.
    Tokens contains details about token usages, costs, and execution time. 
    Use tokens for the questions on these topics. For Example:
        - number of tokens used so far
        - cost of each tokens
        - first name and last name of user who used the toke
        - execution time
        - messages corresponding to each token
        - llm model used for token
    Devices contains the list of devices for the user. The devices can be anything like
        - Sensor
        - Electronics
    Use devices for the questions on these topics. For example:
        - How many devices do I have?
        - Which are the devices with type spare parts?
    If nothing is matching check chat history and find route.
    If chat history is empty or can't find anything use others.
    """

    route_prompt = ChatPromptTemplate(
        messages=[
            SystemMessage(content=system),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}")
        ]
    )
    question_router = route_prompt | structured_llm_router
    return question_router