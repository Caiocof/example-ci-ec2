from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.schemas.current_account import CurrentAccountCreate


account_router = APIRouter(prefix='/account')


@account_router.post('/', response_model=CurrentAccountCreate)
def handle_create_account(
    data: CurrentAccountCreate,
    db: Session = Depends(get_db)
):
    """
    This route is used for creating new current accounts.
    """
    return data
