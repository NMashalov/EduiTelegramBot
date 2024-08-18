import asyncio
import logging

import uvicorn

from chat.settings import AppSettings
from chat.web import create_app

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)


# Запуск бота
async def main():
    create_app()

    uvicorn.run(AppSettings)


if __name__ == "__main__":
    uvicorn.start(main())
