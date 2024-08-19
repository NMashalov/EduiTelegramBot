import asyncio
import logging

import uvicorn

from chat.settings import AppSettings
from chat.web import create_app
from

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)

def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()
# Запуск бота
async def main():
    create_app()

    uvicorn.run(AppSettings)


if __name__ == "__main__":
    uvicorn.start(main())
