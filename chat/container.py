from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from chat.assistant.langfuse.client import LangFuseClient
from chat.assistant.langfuse.settings import LangFuseSettings
from chat.assistant.llm import CodeAssistant
from chat.bot.bot import AppBot
from chat.db.db import SqlAlchemyManager
from chat.db.repository import UserRepository
from chat.db.settings import DbSettings
from chat.scheduler.notify import NotifyBotScheduler


class LangfuseContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    langfuse_client = providers.Singleton(
        LangFuseClient,
        api_key=config.api_key, 
        timeout=config.timeout,
    )

    service = providers.Factory(
        Service,
        api_client=api_client,
    )


class DbConatiner(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(SqlAlchemyManager)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

class LLMContainer(containers.DeclarativeContainer):

    config = providers.Configuration()  

    llm_client = providers.Singleton(
    )

    db =  providers.Singleton(
    )

class AppContainer(containers.DeclarativeContainer):
    def register_bot(self):
        self.register(AppBot, scope=Scope.singleton)
        return self



    def register_langfuse(self):
        self.register(LangFuseSettings, scope=Scope.singleton)
        self.register(LangFuseClient, scope=Scope.singleton)
        return self

    def register_llm(self):
        self.register(CodeAssistant, scope=Scope.singleton)
        return self

    def register_scheduler(self):
        self.register(NotifyBotScheduler, scope=Scope.singleton)
        return self


def prepare_container():
    return (
        AppContainer().register_bot().register_db().register_langfuse().register_llm()
    )
