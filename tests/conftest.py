import asyncio
import json

import pytest
from sqlalchemy import insert
from main import app as fastapi_app
from config import Base, Settings, engine, SessionLocal
from models import RequestWallet
from httpx import AsyncClient, ASGITransport

settings = Settings()


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def open_mock_json(model: str):
        with open(f"tests/fixtures/mock_{model}.json", "r", encoding="utf-8") as file:
            return json.load(file)

    request_wallets = open_mock_json("request_wallets")

    with SessionLocal() as session:
        add_wallets = insert(RequestWallet).values(request_wallets)
        session.execute(add_wallets)
        session.commit()


@pytest.fixture(scope="session")
async def event_loop(request) :
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def session():
    with SessionLocal as session:
        yield session
