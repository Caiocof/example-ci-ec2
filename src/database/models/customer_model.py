from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from src.database.config import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now())
    udpated_at = Column(DateTime, nullable=True)
