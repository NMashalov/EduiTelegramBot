from chat.db.db import DbManager


class UserCrud:
    def __init__(self, db_manager: DbManager):
        self.db_magager = db_manager

    def get_registered(self):
        pass
