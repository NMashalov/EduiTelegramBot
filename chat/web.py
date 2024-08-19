from contextlib import asynccontextmanager

import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chat.container import prepare_container
from chat.db.db import DbManager
from chat.routers.webhook import AiogramRouterFactory
from chat.settings import AppSettings


class WebApp:
    def __init__(self, db_manager: DbManager):
        self.db_manager = db_manager

    @asynccontextmanager
    def lifespan(self, app: FastAPI):
        self.db_manager
        yield

    def create_app(self):
        app = FastAPI(lifespan=self.lifespan)

        app.add_middleware(
            CORSMiddleware,
            allow_origins="*",
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.include_router(AiogramRouterFactory().create_router())
        return app


class UvicornApp:
    def __init__(self, app: WebApp, app_settings: AppSettings):
        self.app = app
        self.app_settings = app_settings

    def start(self):
        uvicorn.run(
            self.app.create_app(),
            port=self.app_settings.port,
            host=self.app_settings.host,
        )
