from sqlalchemy import Boolean, Column, Integer, String
from database.db_handler import Base


class Machine(Base):

    __tablename__ = "machine"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    machine_id = Column(Integer, unique=True, index=True, nullable=False)
    machine_type = Column(Integer, index=True, nullable=False, default=0)
    machine_number = Column(Integer, index=True, nullable=False)
    machine_status = Column(Boolean, nullable=False, default=False)