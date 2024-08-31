import logging

from chat.web import UvicornApp

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)

UvicornApp(
    app=

).start()
