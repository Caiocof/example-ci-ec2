from pydantic import BaseModel


class CurrentAccountBase(BaseModel):
    id: str

    class Config:
        orm_mode = True


class CurrentAccountCreate(BaseModel):
    customerID: str
    initialCredit: float = 0.0
