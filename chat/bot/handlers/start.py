from aiogram import Router
from aiogram.types import Message

from chat.db.db import DbManager


class StartHandlers:
    def __init__(self, db_manager: DbManager):
        self.db_manager = db_manager
        self.router = Router()

    async def hi(self, message: Message):
        await message.answer()
