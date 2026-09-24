import aiohttp_jinja2
from aiohttp import web

from notes import __version__

MAX_LENGTH = 500


def _storage(request):
    return request.app["storage"]


def _clean_text(value):
    text = (value or "").strip()
    if not text:
        raise web.HTTPBadRequest(text="Текст заметки не может быть пустым")
    if len(text) > MAX_LENGTH:
        raise web.HTTPBadRequest(text=f"Максимум {MAX_LENGTH} символов")
    return text


@aiohttp_jinja2.template("index.html")
async def index(request):
    return {"notes": _storage(request).list()}


async def create_note_form(request):
    data = await request.post()
    _storage(request).add(_clean_text(data.get("text")))
    raise web.HTTPFound(request.app.router["index"].url_for())


async def api_list(request):
    return web.json_response([n.to_dict() for n in _storage(request).list()])


async def api_create(request):
    try:
        payload = await request.json()
    except ValueError:
        raise web.HTTPBadRequest(text="Ожидается JSON")
    note = _storage(request).add(_clean_text(payload.get("text")))
    return web.json_response(note.to_dict(), status=201)


async def api_detail(request):
    note = _storage(request).get(int(request.match_info["id"]))
    if note is None:
        raise web.HTTPNotFound()
    return web.json_response(note.to_dict())


async def api_delete(request):
    if not _storage(request).delete(int(request.match_info["id"])):
        raise web.HTTPNotFound()
    return web.Response(status=204)


async def health(request):
    return web.json_response({"status": "ok", "version": __version__})
