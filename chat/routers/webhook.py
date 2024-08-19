from fastapi import APIRouter

from chat.bot.bot import AppBot


class AiogramRouterFactory:
    AIOGRAM_PREFIX: str = "/webhook"

    TAGS = ["aiogram", "webhook"]

    def __init__(self, bot: AppBot):
        self.bot = bot

    def register_tg(self):
        self.bot.dp.include_routers()

        self.bot.set_webhook(
            prefix=self.AIOGRAM_PREFIX,
        )

    def create_router(self):
        self.register_tg()
        router = APIRouter(tags=self.TAGS)

        router.add_api_route(self.AIOGRAM_PREFIX, self.bot.feed_update)
