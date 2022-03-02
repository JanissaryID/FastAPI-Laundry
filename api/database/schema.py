import string
from typing import Optional
from pydantic import BaseModel


class MachineBase(BaseModel):
    machine_type: int
    machine_number: int
    machine_status: bool
    machine_grade: bool
    machine_price: str


class MachineAdd(MachineBase):
    machine_id: int

    class Config:
        orm_mode = True


class Machine(MachineAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateMachine(BaseModel):
    machine_status: bool

    class Config:
        orm_mode = True

class UpdatePriceMachine(BaseModel):
    machine_type: int
    machine_number: int
    machine_grade: bool
    machine_price: str

    class Config:
        orm_mode = True