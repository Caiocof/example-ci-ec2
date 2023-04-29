from sqlalchemy.orm import Session
from sqlalchemy import update

from src.crud.base_crud import BaseCRUD
from src.database.models.customer_model import Customer
from src.schemas.customer_schema import CustomerCreate


class CustomerCRUD(BaseCRUD):

    def create(self, db: Session, customer_data: CustomerCreate):
        db_customer = Customer(**dict(customer_data))
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer

    def delete(self, db: Session, customer_id: str):
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        db.delete(customer)
        db.commit()
        return

    def get(self, db: Session, customer_id: str):
        db_customer = db.query(Customer).filter_by(id=customer_id).first()
        return db_customer

    def list(self, db: Session):
        records = db.query(Customer).all()
        return records

    def patch(self, db: Session, id: str, customer_data: CustomerCreate):
        db.execute(
            update(Customer).where(Customer.id == id)
            .values(**dict(customer_data))
        )
        db.commit()
        return
