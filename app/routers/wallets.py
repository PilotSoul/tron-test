from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from tronpy.exceptions import AddressNotFound, BadAddress

from config import get_db
from decorators import save_wallet_to_db
from queries import RequestWalletQuery
from schemas import WalletInfoRequest, WalletInfoResponse, WalletRequestRecord
from services.tron import get_wallet_resources

router = APIRouter(prefix="/wallet")


@router.post("", response_model=WalletInfoResponse)
@save_wallet_to_db
async def get_wallet_info(
    request: WalletInfoRequest, db: Session = Depends(get_db)
) -> WalletInfoResponse:
    try:
        tron_info = await get_wallet_resources(request.wallet_address)

        return WalletInfoResponse(
            wallet_address=request.wallet_address,
            balance_trx=tron_info["balance"] / 1_000_000,
            energy=tron_info["energy"],
            bandwidth=tron_info["bandwidth"],
        )
    except (AddressNotFound, BadAddress):
        raise HTTPException(status_code=404, detail="Wallet not found")


@router.get("/requests", response_model=list[WalletRequestRecord])
def read_requests(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=1000),
    db: Session = Depends(get_db),
):
    return RequestWalletQuery.get_all(db, skip=skip, limit=limit)
