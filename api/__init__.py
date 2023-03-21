import os
from fastapi import FastAPI
from api.base.endpoints import root, demo_api

app = FastAPI(
    title=os.getenv("FASTAPI_TITLE", "Narwhal"),
    description=os.getenv("FASTAPI_DESC", "Narwhal"),
    version=os.getenv("VERSION", "DEVELOPMENT"))

app.include_router(root.router)
app.include_router(demo_api.router)