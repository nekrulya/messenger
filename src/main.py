from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.config import settings
from src.database import create_tables

from src.auth.router import router as router_auth
from src.chat.router import router as router_chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Before app started")
    await create_tables()
    yield
    print("After app started")

app = FastAPI(
    debug=settings.DEBUG,
    title="Наспамили",
    version=settings.VERSION,
    lifespan=lifespan
)

app.include_router(router_auth)
app.include_router(router_chat)

@app.get("/")
async def home() -> RedirectResponse:
    return RedirectResponse("/docs")
