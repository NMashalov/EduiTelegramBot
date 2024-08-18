from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message


class OnlyRegisteredMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        self.counter += 1

        data["counter"] = self.counter
        return await handler(event, data)


class OnlyPrivateMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if event.chat.type == "private":
            return await handler(event, data)


class OnlyRegisteredMiddleware(BaseMiddleware):
    GOOD_IDS: list[int] = [100]

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if user := event.from_user:
            if user.id in self.GOOD_IDS:
                return await handler(event, data)
