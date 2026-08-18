import os

from langchain_groq import ChatGroq

from agents.State import AgentState
from tools import create_tasks, get_task_from_db

llm = ChatGroq(model="openai/gpt-oss-safeguard-20b", temperature=0)

llm_with_tool = llm.bind_tools([get_task_from_db, create_tasks])


async def call_agent(state: AgentState) -> AgentState:
    # messages = state.get("messages").copy()  # type: ignore  commented since messages is annotated with reducer
    result = await llm_with_tool.ainvoke(state["messages"])
    return {"messages": [result]}
