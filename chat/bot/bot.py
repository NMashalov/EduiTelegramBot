from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, Update
from fastapi.requests import Request


class AppBot:
    def __init__(self):
        self.bot = Bot(token="TOKEN")
        self.dp = Dispatcher()

    async def set_webhook(self, prefix: str):
        await self.bot.set_webhook(
            url=prefix,
            allowed_updates=self.dp.resolve_used_update_types(),
            drop_pending_updates=True,
        )

    def registe_router(self, router: Router):
        self.dp.include_router()

    async def feed_update(self, request: Request):
        req = await request.json()
        update = Update.model_validate(req, context={"bot": self.bot})
        await self.dp.feed_update(self.bot, update)

    async def send(self, chat_id: int, text: str):
        self.bot.send_message(chat_id, text=text)
