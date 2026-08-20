import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

from agents.Graph import graph
from routes.Chat import router

DB_URL = os.getenv("DATABASE_URL")


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncPostgresSaver.from_conn_string(DB_URL) as checkpointer:
        await checkpointer.setup()

        app.state.graph = graph.compile(checkpointer=checkpointer)

        yield


app = FastAPI(title="CoOps", version="1", lifespan=lifespan)

app.include_router(router=router)
