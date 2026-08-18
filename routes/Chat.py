from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

from agents.Graph import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    thread_id: str


@router.post("/chat")
async def chat_agent(request: ChatRequest):
    if not request.message or not request.message.strip() or not request.thread_id:
        raise HTTPException(status_code=400, detail="Empty Fields are not Allowed")
    config = {"configurable": {"thread_id": request.thread_id}}
    response = await graph.ainvoke(
        {"messages": HumanMessage(content=request.message)}, config=config
    )
    return {"response": response["messages"][-1]}
