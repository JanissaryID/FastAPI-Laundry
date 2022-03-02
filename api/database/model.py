from sqlalchemy import Boolean, Column, Integer, String
from database.db_handler import Base

class TransactionsModel(Base):

    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    type = Column(String, nullable=False, default="null")
    number = Column(Integer, index=True, nullable=False)
    date = Column(String, nullable=False, default="1-1-2000")
    time = Column(String, nullable=False, default="00:00")
    price = Column(String, nullable=False, default="0")

class Machine(Base):

    __tablename__ = "machine"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    machine_id = Column(Integer, unique=True, index=True, nullable=False)
    machine_type = Column(Integer, index=True, nullable=False, default=0)
    machine_number = Column(Integer, index=True, nullable=False)
    machine_status = Column(Boolean, nullable=False, default=False)
    machine_grade = Column(Boolean, nullable=False, default=False)
    machine_price = Column(String, nullable=False, default="0")
    

