import pytest

from notes.main import create_app


@pytest.fixture
async def client(aiohttp_client):
    return await aiohttp_client(create_app())
