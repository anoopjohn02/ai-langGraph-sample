from langchain_core.tools import tool

from app.ai.vectors import build_retriever


@tool
def vector_tool(query):
    """
    Use this tool when query contains details about spices. Pass the query to the tool.
    """
    retriever = build_retriever()
    results = retriever.get_relevant_documents(query)
    return results
