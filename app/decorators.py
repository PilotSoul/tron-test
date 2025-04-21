from functools import wraps

from fastapi import Depends
from sqlalchemy.orm import Session

from config import get_db
from queries import RequestWalletQuery


def save_wallet_to_db(func):
    """Декоратор для записи кошелька в БД"""

    @wraps(func)
    async def wrapper(*args, db: Session = Depends(get_db), **kwargs):
        response = await func(*args, db=db, **kwargs)

        RequestWalletQuery.create(
            db=db,
            wallet_address=response.wallet_address,
            balance=int(response.balance_trx * 1_000_000),
            energy=response.energy,
            bandwidth=response.bandwidth,
        )
        return response

    return wrapper
