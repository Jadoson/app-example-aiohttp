import logging
from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web

from notes import config
from notes.middlewares import timing_middleware
from notes.routes import setup_routes
from notes.storage import NoteStorage

TEMPLATES_DIR = Path(__file__).parent / "templates"


async def seed_notes(app):
    app["storage"].add("Первая заметка — приложение работает")


def create_app():
    logging.basicConfig(level=logging.INFO)
    app = web.Application(middlewares=[timing_middleware])
    app["storage"] = NoteStorage()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
        context_processors=[aiohttp_jinja2.request_processor],
    )
    aiohttp_jinja2.get_env(app).globals["app_title"] = config.APP_TITLE
    setup_routes(app)
    app.on_startup.append(seed_notes)
    return app
