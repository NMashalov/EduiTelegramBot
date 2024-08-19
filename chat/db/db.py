import logging
from contextlib import asynccontextmanager
from typing import Callable

from langchain_postgres import PostgresChatMessageHistory
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from chat.db.models.base import Base
from chat.db.settings import DbSettings

logger = logging.getLogger(__name__)


class DbManager:
    CHAT_TABLE_NAME = "CHAT"

    def __init__(self, settings: DbSettings):
        self.a_sqlalchemy_engine = create_async_engine(settings.conn_string, echo=True)
        self.a_sessionmaker = async_sessionmaker(
            self.a_sqlalchemy_engine, expire_on_commit=False
        )

    @asynccontextmanager
    async def create_message_history(
        self,
        session_id: str,
    ):
        async with self.a_sqlalchemy_engine.begin() as a_conn:
            yield PostgresChatMessageHistory(
                self.CHAT_TABLE_NAME, session_id, async_connection=a_conn
            )

    @asynccontextmanager
    async def a_session(self):
        session = self.a_sessionmaker()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
        finally:
            session.close()

    async def init_models(self):
        async with self.a_sqlalchemy_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
