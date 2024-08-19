from aiogram import Bot, Dispatcher, F
from fastapi import APIRouter


class LlmRouterFactory:
    AIOGRAM_PREFIX: str = "/llm"

    TAGS = ["llm"]

    def __init__(self, bot: Bot):
        self.bot = bot

    def create_router(self):
        router = APIRouter(tags=self.TAGS)

        router.add_api_route(AIOGRAM_PREFIXs)
