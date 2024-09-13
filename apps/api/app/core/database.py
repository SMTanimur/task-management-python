from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from .config  import DB_HOST, DB_USER, DB_PASS,DB_NAME,DB_PORT
# Database onnection string
DATABASE_URL = (
    f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

engine_async = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine_async,class_=AsyncSession, expire_on_commit=False)

engine_sync = create_engine(DATABASE_URL)
sync_session_maker = sessionmaker(engine_sync)
