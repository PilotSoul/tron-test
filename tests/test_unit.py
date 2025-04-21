from unittest.mock import MagicMock
import pytest
from app.queries import RequestWalletQuery
from models import RequestWallet


def test_create_wallet_request_unit():
    """Unit тест на запись кошелька в БД"""
    mock_db = MagicMock()
    wallet_address = "TXYZ123"
    balance = 1000000
    energy = 5
    bandwidth = 8475

    result = RequestWalletQuery.create(mock_db, wallet_address, balance, energy, bandwidth)

    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()
    assert isinstance(result, RequestWallet)
    assert result.wallet_address == wallet_address