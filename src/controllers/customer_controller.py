from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.crud.customer_crud import CustomerCRUD
from src.schemas.customer_schema import CustomerCreate
from src.controllers.BaseController import BaseController


class CustomerController(BaseController):

    @staticmethod
    def handle_create(db: Session, data: CustomerCreate):
        return CustomerCRUD().create(db, data)

    @staticmethod
    def handle_get(db: Session, customer_id: str):
        return CustomerCRUD().get(db, customer_id)

    @staticmethod
    def handle_list(db: Session):
        return CustomerCRUD().list(db)

    @staticmethod
    def handle_delete(db: Session, customer_id: str):
        db_customer = CustomerCRUD().get(db, customer_id)

        if db_customer is None:
            raise HTTPException(
                status_code=404,
                detail={'message': 'resource not found'}
            )

        return CustomerCRUD().delete(db, customer_id)

    @staticmethod
    def handle_patch(db: Session, id: str, customer_data: CustomerCreate):
        db_customer = CustomerCRUD().get(db, id)

        if db_customer is None:
            raise HTTPException(
                status_code=404,
                detail={'message': 'resource not found'}
            )

        return CustomerCRUD().patch(db, id, customer_data)
