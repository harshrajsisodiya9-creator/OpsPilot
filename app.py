from fastapi import FastAPI

from routes.Chat import router

app = FastAPI(title="CoOps", version="1")

app.include_router(router=router)
