from typing import Annotated

from fastapi import APIRouter, Depends

from src.auth.router import oauth2_scheme

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/")
async def chats(token: Annotated[str, Depends(oauth2_scheme)]):
    pass