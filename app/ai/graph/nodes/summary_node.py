from typing import Any, Dict

from langchain_core.messages import HumanMessage

from app.ai.graph.state import GraphState
from app.ai.llms import build_llm
from app.services.conversation import save_conversation_summary


def save_summary_node(state: GraphState) -> Dict[str, Any]:
    print("---SUMMARY NODE---")
    conversation_id = state["conversation_id"]
    summary = state.get("conv_summary", "")
    if summary:
        summary_message = (
            f"This is a summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into account the new messages above:"
        )
    else:
        summary_message = "Create a summary of the conversation above:"

    llm = build_llm(state, False)
    messages = state["messages"] + [HumanMessage(content=summary_message)]
    response = llm.invoke(messages)
    save_conversation_summary(conversation_id, response.content)
    return {"conv_summary": response.content}