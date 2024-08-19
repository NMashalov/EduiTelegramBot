from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chat.container import prepare_container
from chat.routers.llm import Control
from chat.settings import AppSettings


class WebApp:
    def __init__(self, app_seetings: AppSettings ):
        self.app_settings = self.app_settings

    @asynccontextmanager
    def lifespan(app: FastAPI):
        prepare_container()
        yield


    def create_app(routers: list[APIRouter]):
        app = FastAPI()

        app.add_middleware(
            CORSMiddleware,
            allow_origins="*",
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.include_router(Control.create_router())


class WebApp:
    def __init__(self, app_seetings: AppSettings ):
        self.app_settings = self.app_settings

    @asynccontextmanager
    def lifespan(app: FastAPI):
        prepare_container()
        yield


    def start_app(routers: list[APIRouter]):
        pass
