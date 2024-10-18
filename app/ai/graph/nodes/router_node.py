from app.ai.chains.router import RouteQuery, build_llm_router
from app.ai.graph.consts import DOCUMENT, TOKEN, DEVICES, OTHERS
from app.ai.graph.state import GraphState
from app.services.conversation import get_conversation_summary


def route_question_node(state: GraphState) -> str:
    print("---ROUTE QUESTION---")
    question = state["question"]
    conversation_id = state["conversation_id"]
    summary = get_conversation_summary(conversation_id)
    router = build_llm_router(state)
    source: RouteQuery = router.invoke({"question": question, "chat_history": [summary]})
    if source.datasource == "vectorstore":
        print("---ROUTE QUESTION TO VECTOR STORE---")
        return DOCUMENT
    elif source.datasource == "tokens":
        print("---ROUTE QUESTION TO TOKEN---")
        return TOKEN
    elif source.datasource == "devices":
        print("---ROUTE QUESTION TO DEVICES---")
        return DEVICES
    elif source.datasource == "others":
        print("---ROUTE QUESTION TO OTHERS---")
        return OTHERS