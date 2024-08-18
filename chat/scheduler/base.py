import asyncio

import schedule


class BaseBotScheduler:
    def __init__(self):
        self.scheduler = schedule.Scheduler()

    def timetable(self):
        pass

    async def serve_forever(self):
        while True:
            await self.scheduler.run_pending()
            await asyncio.sleep(1)
