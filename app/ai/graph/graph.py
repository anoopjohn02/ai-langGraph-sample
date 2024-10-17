
from langgraph.graph import END, StateGraph

from .consts import DOCUMENT, TOKEN, DEVICES, GENERATE
from .nodes import retrieve_document_node, user_devices_node, token_usage_node, generate_output_node
from .state import GraphState
from ..chains.router import RouteQuery
from ..chains.router import build_llm_router


def route_question(state: GraphState) -> str:
    print("---ROUTE QUESTION---")
    question = state["question"]
    router = build_llm_router(state)
    source: RouteQuery = router.invoke({"question": question})
    if source.datasource == "vectorstore":
        print("---ROUTE QUESTION TO VECTOR STORE---")
        return DOCUMENT
    elif source.datasource == "tokens":
        print("---ROUTE QUESTION TO TOKEN---")
        return TOKEN
    elif source.datasource == "devices":
        print("---ROUTE QUESTION TO DEVICES---")
        return DEVICES


workflow = StateGraph(GraphState)

workflow.add_node(DOCUMENT, retrieve_document_node)
workflow.add_node(TOKEN, token_usage_node)
workflow.add_node(DEVICES, user_devices_node)
workflow.add_node(GENERATE, generate_output_node)

workflow.set_conditional_entry_point(
    route_question,
    {
        DOCUMENT: DOCUMENT,
        TOKEN: TOKEN,
        DEVICES: DEVICES
    },
)
workflow.add_edge(DOCUMENT, GENERATE)
workflow.add_edge(TOKEN, GENERATE)
workflow.add_edge(DEVICES, GENERATE)
workflow.add_edge(GENERATE, END)
app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")