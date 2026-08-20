from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    thread_id: str


async def stream_response(request: ChatRequest, req: Request):

    config = {"configurable": {"thread_id": request.thread_id}}
    try:
        async for event in req.app.state.graph.astream_events(
            {"messages": [HumanMessage(content=request.message)]},
            config=config,
            version="v2",
        ):
            if event["event"] == "on_chat_model_stream":
                chunk = event["data"]["chunk"]
                if chunk.content:
                    yield f"data: {chunk.content}\n\n"

    except Exception as e:
        yield f"event: error {e}"


@router.post("/chat")
async def chat_agent(request: ChatRequest, req: Request):
    if not request.message.strip() or not request.thread_id:
        raise HTTPException(status_code=400, detail="Empty Fields are not Allowed")

    return StreamingResponse(
        content=stream_response(request=request, req=req),
        media_type="text/event-stream",
    )

    # return {"response": response["messages"][-1]}
