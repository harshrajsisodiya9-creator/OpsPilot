from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

from agents.Graph import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_agent(request: ChatRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Empty String not Allowed")
    response = await graph.ainvoke({"messages": HumanMessage(content=request.message)})
    return {"response": response["messages"][-1]}
