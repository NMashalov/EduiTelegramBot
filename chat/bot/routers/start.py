from aiogram import F, Router
from aiogram.filters import Command, CommandStart

from chat.bot.handlers.start import StartHandlers
from chat.bot.middleware import OnlyPrivateMiddleware


class StartRouter:
    NAME = "REGISTRATION"

    def __init__(self):
        self.router = Router(name=self.NAME)

    def register_middlewares(self):
        self.router.message.middleware(OnlyPrivateMiddleware)

    def prepare_router(self):
        self.register_middlewares()
        self.router.message.register(StartHandlers.hi, CommandStart())
        return self.router
