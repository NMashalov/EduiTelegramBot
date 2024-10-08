from datetime import datetime, timedelta

import schedule
import freezegun

def job():
    print("I'm working...")


now = datetime(2020, 1, 1, 10, 31)
with freezegun.freeze_time(now) as frozen_date:
    schedule.every(3).days.at("10:30").do(job)
    schedule.run_pending()  # nothing happens
    frozen_date.move_to(now + timedelta(days=3))
    schedule.run_pending()  # job has run