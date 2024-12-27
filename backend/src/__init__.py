from fastapi import FastAPI

from .config import Settings
from .services.networks.connection import connect_networks


settings = Settings()

app = FastAPI(
    title="Basic RAG simulation",
    description="This is a website used to simulate the basic RAG procedure.",
)

from .routers import page_home

app = connect_networks(app)
app.include_router(page_home.router)