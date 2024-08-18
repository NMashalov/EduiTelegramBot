from aiogram import Bot, Dispatcher, F
from chat.bot.bot import Bot


class AiogramRouterFactory:
    AIOGRAM_PREFIX: str = "/llm"

    TAGS = ["aiogram", "webhook"]

    def __init__(self, bot: Bot):
        self.bot = bot

    async def create_router(self):
        dp.include_routers(questions.router, different_types.router)

        await self.bot.set_webhook(
            url=self.AIOGRAM_PREFIX,
            allowed_updates=self.dp.resolve_used_update_types(),
            drop_pending_updates=True,
        )
