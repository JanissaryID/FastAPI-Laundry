from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import database.crud as crud
import database.model as model
import database.schema as schema
import database.schemaTransactions as schemaTransactions
import database.crudTransactions as crudTransactions
from database.db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Machine Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/machine', response_model=List[schema.Machine])
def retrieve_all_machine_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    machine = crud.get_machine(db=db, skip=skip, limit=limit)
    return machine

@app.get('/transactions', response_model=List[schemaTransactions.Transactions])
def retrieve_all_transactions_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = crudTransactions.get_transactions(db=db, skip=skip, limit=limit)
    return transactions

@app.get('/transaction-filter-date', response_model=List[schemaTransactions.Transactions])
def get_transaction_by_date(date: str, db: Session = Depends(get_db)):
    details = crudTransactions.get_transactions_by_date(db=db, date=date)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        showfilter = crudTransactions.get_transactions_by_date(db=db, date=date)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Transaction: {e}")
    return showfilter

@app.delete('/delete')
def delete_machine_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_machine_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_machine_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update', response_model=schema.Machine)
def update_machine_details(sl_id: int, update_param: schema.UpdateMachine, db: Session = Depends(get_db)):
    details = crud.get_machine_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_machine_details(db=db, details=update_param, sl_id=sl_id)

@app.put('/update-price', response_model=schema.Machine)
def update_price_machine_details(sl_id: int, update_param: schema.UpdatePriceMachine, db: Session = Depends(get_db)):
    details = crud.get_machine_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_price_machine_details(db=db, details=update_param, sl_id=sl_id)

@app.get('/machine-id')
def get_machine_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_machine_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to show")

    try:
        crud.get_machine_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Machine: {e}")
    return crud.get_machine_by_id(db=db, sl_id=sl_id)



@app.post('/add', response_model=schema.MachineAdd)
def add_new_machine(machine: schema.MachineAdd, db: Session = Depends(get_db)):
    machine_id = crud.get_machine_by_machine_id(db=db, machine_id=machine.machine_id)
    if machine_id:
        raise HTTPException(status_code=400, detail=f"Machine id {machine.machine_id} already exist in database: {machine_id}")
    return crud.add_machine_details_to_db(db=db, machine=machine)

@app.post('/add-transaction', response_model=schemaTransactions.TransactionsAdd)
def add_new_transactions(transactions: schemaTransactions.TransactionsAdd, db: Session = Depends(get_db)):
    # transactions_id = crudTransactions.get_transactions_by_transactions_date(db=db, transacrions_date=transactions.date)
    # if transactions_id:
    #     raise HTTPException(status_code=400, detail=f"Transactions id {transactions.id} already exist in database: {id}")
    return crudTransactions.add_transactions_details_to_db(db=db, transactions=transactions)