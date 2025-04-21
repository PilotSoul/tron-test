from sqlalchemy import BigInteger, Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declared_attr

from config import Base


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )


class RequestWallet(TimestampMixin, Base):
    __tablename__ = "request_wallet"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True, nullable=False)
    balance = Column(BigInteger)
    energy = Column(Integer)
    bandwidth = Column(Integer)
