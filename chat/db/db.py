from contextlib import asynccontextmanager

from langchain_postgres import PostgresChatMessageHistory
from psycopg import AsyncConnection
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from chat.db.models.base import Base
from chat.db.settings import DbSettings


class DbManager:
    def __init__(self, settings: DbSettings):
        self.settings = settings

    @asynccontextmanager
    async def connection(self):
        async with AsyncConnection() as conn:
            yield conn


class ChatHistoryManager(DbManager):
    CHAT_TABLE_NAME = "CHAT"

    @asynccontextmanager
    async def create_message_history(
        self,
        session_id: str,
    ):
        async with self.connection() as a_conn:
            yield PostgresChatMessageHistory(
                self.CHAT_TABLE_NAME, session_id, async_connection=a_conn
            )


class SqlAlchemyManager(DbManager):
    def __init__(self, settings: DbSettings):
        super().__init__(settings)
        self.a_sqlalchemy_engine = create_async_engine(
            self.settings.conn_string, echo=True
        )
        self.a_sessionmaker = sessionmaker(
            self.a_sqlalchemy_engine, class_=AsyncSession, expire_on_commit=False
        )

    def a_session(self):
        return self.a_sessionmaker()

    async def init_models(self):
        async with self.a_sqlalchemy_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
