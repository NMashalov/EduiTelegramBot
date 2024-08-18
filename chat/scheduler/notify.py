from chat.bot.bot import Bot
from chat.db.db import DbManager
from chat.scheduler.base import BaseBotScheduler


class NotifyBotScheduler(BaseBotScheduler):
    def __init__(self, bot: Bot, db_manager: DbManager):
        super().__init__()
        self.bot = bot
        self.db_manager = db_manager

    async def notify_registered(self):
        await self.db_manager
        self.bot.send_message()

    def timetable(self):
        self.scheduler.every().minute.do(self.notify_registered)
