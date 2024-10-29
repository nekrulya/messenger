from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Before app started")
    yield
    print("After app started")

app = FastAPI(
    debug=settings.debug,
    title="Наспамили",
    version=settings.version,
    lifespan=lifespan
)

