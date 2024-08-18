from punq import Container, Scope

from chat.db.db import DbManager
from chat.db.settings import DbSettings


class AppContainer(Container):
    def register_db(self):
        self.register(DbSettings, scope=Scope.singleton)
        self.register(DbManager, scope=Scope.singleton)
        return self

    def register_llm(self):
        pass


def prepare_container():
    AppContainer().register_db()
