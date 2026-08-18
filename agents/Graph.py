from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from agents.LLm import call_agent
from agents.routing import should_continue
from agents.State import AgentState
from agents.ToolNode import tasks_tools

checkpointer = MemorySaver()

builder = StateGraph(AgentState)

builder.add_node("llm", call_agent)
builder.add_edge(START, "llm")
builder.add_node("tasktool", tasks_tools)
builder.add_conditional_edges(
    "llm",
    should_continue,
    {
        "tasktool": "tasktool",  # if should_continue returns string named "tasktool" go to tasktool node
        "end": END,  # if no tool call is there we go to end instead of tasktool
    },
)
builder.add_edge("tasktool", "llm")
graph = builder.compile(checkpointer=checkpointer)
