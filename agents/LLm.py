import os

from langchain_groq import ChatGroq

from agents.State import AgentState

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


async def call_agent(state: AgentState) -> AgentState:
    result = await llm.ainvoke(state.get("user_message"))
    return {"response": result.content}
