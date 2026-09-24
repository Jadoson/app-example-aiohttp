from pathlib import Path

from notes import views

STATIC_DIR = Path(__file__).parent / "static"


def setup_routes(app):
    app.router.add_get("/", views.index, name="index")
    app.router.add_post("/notes", views.create_note_form)
    app.router.add_get("/api/notes", views.api_list)
    app.router.add_post("/api/notes", views.api_create)
    app.router.add_get(r"/api/notes/{id:\d+}", views.api_detail)
    app.router.add_delete(r"/api/notes/{id:\d+}", views.api_delete)
    app.router.add_get("/health", views.health)
    app.router.add_static("/static/", STATIC_DIR, name="static")
