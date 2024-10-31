from sqlalchemy.orm import DeclarativeBase

from src.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(url=settings.database.url)

class Base(DeclarativeBase):
    pass

from src.auth.models import *

async def create_tables():
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
    except BaseException as e:
        print(f"Произошла ошибка: {e}")

get_session = async_sessionmaker(engine)

