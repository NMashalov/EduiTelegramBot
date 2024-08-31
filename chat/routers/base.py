from fastapi import APIRouter

class BaseRouterFactory:
    def create_router(self) -> APIRouter:
        pass