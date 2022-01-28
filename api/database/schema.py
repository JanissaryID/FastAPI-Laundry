from typing import Optional
from pydantic import BaseModel


class MachineBase(BaseModel):
    machine_type: int
    machine_number: int
    machine_status: bool


class MachineAdd(MachineBase):
    machine_id: int
    # streaming_platform: Optional[str] = None
    # membership_required: bool

    class Config:
        orm_mode = True


class Machine(MachineAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateMachine(BaseModel):
    machine_status: bool
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    # streaming_platform: Optional[str] = None
    # membership_required: bool

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True