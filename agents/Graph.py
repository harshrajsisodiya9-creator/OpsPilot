from langgraph.graph import END, START, StateGraph

from agents.LLm import call_agent
from agents.State import AgentState

builder = StateGraph(AgentState)

builder.add_node("llm", call_agent)
builder.add_edge(START, "llm")
builder.add_edge("llm", END)
graph = builder.compile()
