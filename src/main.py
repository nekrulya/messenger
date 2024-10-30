from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings
from src.database import create_tables


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

@app.get("/")
async def home():
    return {"data": "Hello"}
