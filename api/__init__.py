import os
from fastapi import FastAPI
from api.base.endpoints import root, template_api

app = FastAPI(
    title=os.getenv("FASTAPI_TITLE", "API Template"),
    description=os.getenv("FASTAPI_DESC", "API Template for MongoDB"),
    version=os.getenv("VERSION", "DEVELOPMENT"),
)

app.include_router(root.router)
app.include_router(template_api.router)
