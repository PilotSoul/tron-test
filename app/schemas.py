from datetime import datetime

from pydantic import BaseModel


class WalletInfoRequest(BaseModel):
    wallet_address: str


class WalletInfoResponse(BaseModel):
    wallet_address: str
    balance_trx: float
    energy: int
    bandwidth: int


class WalletRequestRecord(BaseModel):
    id: int
    wallet_address: str
    created_at: datetime
    balance: float
    energy: int
    bandwidth: int
