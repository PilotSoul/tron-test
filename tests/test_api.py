from httpx import AsyncClient
import pytest


async def test_wallet_info(ac: AsyncClient):
    test_address = "TBia4uHnb3oSSZm5isP284cA7Np1v15Vhi"
    response = await ac.post("/api/wallet", json={"wallet_address": test_address})
    assert response.status_code == 200
    assert "balance_trx" in response.json()