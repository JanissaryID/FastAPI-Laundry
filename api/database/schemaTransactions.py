from typing import Optional
from pydantic import BaseModel


class TransactionsBase(BaseModel):
    
    number: int
    date: str
    time: str
    price: str


class TransactionsAdd(TransactionsBase):
    # id: int
    type: str

    class Config:
        orm_mode = True


class Transactions(TransactionsAdd):
    # id: int
    type: str

    class Config:
        orm_mode = True


# class UpdateTransactions(BaseModel):
#     machine_status: bool

#     class Config:
#         orm_mode = True