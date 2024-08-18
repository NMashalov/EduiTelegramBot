from aiogram import F, Router

from chat.bot.handlers.registration import RegistrationHandlers
from chat.bot.middleware import OnlyPrivateMiddleware


class StartRouter:
    NAME = "REGISTRATION"

    def __init__(self):
        self.router = Router(name=self.NAME)

    def register_middlewares(self):
        self.router.message.middleware(OnlyPrivateMiddleware)

    def prepare_router(self):
        self.register_middlewares()
        self.router.message.register(RegistrationHandlers.answer_yes, CommandStart())
        return self.router
