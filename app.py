from aiohttp import web

from notes import config
from notes.main import create_app

if __name__ == "__main__":
    web.run_app(create_app(), host=config.HOST, port=config.PORT)
