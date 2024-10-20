
from langgraph.graph import END, StateGraph

from .consts import DOCUMENT, TOKEN, DEVICES, GENERATE, OTHERS, HISTORY, SUMMARY, REFINE
from .nodes import (retrieve_document_node, route_question_node, user_devices_node,
                    token_usage_node, generate_output_node, other_node, save_history_node,
                    save_summary_node, refine_question_node)
from .state import GraphState

workflow = StateGraph(GraphState)

workflow.add_node(REFINE, refine_question_node)
workflow.add_node(DOCUMENT, retrieve_document_node)
workflow.add_node(TOKEN, token_usage_node)
workflow.add_node(DEVICES, user_devices_node)
workflow.add_node(GENERATE, generate_output_node)
workflow.add_node(OTHERS, other_node)
workflow.add_node(HISTORY, save_history_node)
workflow.add_node(SUMMARY, save_summary_node)

workflow.set_conditional_entry_point(
    route_question_node,
    {
        DOCUMENT: REFINE,
        TOKEN: TOKEN,
        DEVICES: DEVICES,
        OTHERS: OTHERS
    },
)
workflow.add_edge(REFINE, DOCUMENT)
workflow.add_edge(DOCUMENT, GENERATE)
workflow.add_edge(TOKEN, GENERATE)
workflow.add_edge(DEVICES, GENERATE)
workflow.add_edge(OTHERS, GENERATE)
workflow.add_edge(GENERATE, HISTORY)
workflow.add_edge(HISTORY, SUMMARY)
workflow.add_edge(SUMMARY, END)
graph = workflow.compile()
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")