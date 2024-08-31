from fastapi.requests import Request
from aiogram.types import  Update
from chat.bot.bot import Bot


class BotHandler:
    def __init__(self,bot: Bot):
        self.bot = bot

    async def webhook(self,request: Request) -> None:
        await self.bot.feed_update(request=request)