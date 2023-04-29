from datetime import datetime
from uuid import UUID

from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class CustomerCreate(BaseModel):
    name: str
    surname: str

    class Config:
        orm_mode = True


class CustomerResponse(CustomerBase):
    name: str
    surname: str
    created_at: datetime
    updated_at: Optional[datetime]
