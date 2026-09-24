async def test_index(client):
    resp = await client.get("/")
    assert resp.status == 200
    assert "Первая заметка" in await resp.text()


async def test_health(client):
    resp = await client.get("/health")
    assert (await resp.json())["status"] == "ok"


async def test_api_crud(client):
    resp = await client.post("/api/notes", json={"text": "hello"})
    assert resp.status == 201
    note_id = (await resp.json())["id"]

    resp = await client.get(f"/api/notes/{note_id}")
    assert (await resp.json())["text"] == "hello"

    resp = await client.delete(f"/api/notes/{note_id}")
    assert resp.status == 204
    resp = await client.get(f"/api/notes/{note_id}")
    assert resp.status == 404


async def test_form_submit(client):
    resp = await client.post("/notes", data={"text": "из формы"}, allow_redirects=False)
    assert resp.status == 302
    assert "из формы" in await (await client.get("/")).text()


async def test_empty_note_rejected(client):
    resp = await client.post("/api/notes", json={"text": "  "})
    assert resp.status == 400
