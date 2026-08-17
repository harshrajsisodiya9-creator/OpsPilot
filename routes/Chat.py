from fastapi import APIRouter
from pydantic import BaseModel

from agents.Graph import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_agent(request: ChatRequest):
    response = await graph.ainvoke({"user_message": request.message})
    return {"response": response.get("response")}
