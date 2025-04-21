from sqlalchemy.orm import Session

from models import RequestWallet


class RequestWalletQuery:
    @staticmethod
    def create(
        db: Session, wallet_address: str, balance: int, energy: int, bandwidth: int
    ):
        db_request = RequestWallet(
            wallet_address=wallet_address,
            balance=balance,
            energy=energy,
            bandwidth=bandwidth,
        )
        db.add(db_request)
        db.commit()
        db.refresh(db_request)
        return db_request

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return (
            db.query(RequestWallet)
            .order_by(RequestWallet.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
