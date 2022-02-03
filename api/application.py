from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import database.crud as crud
import database.model as model
import database.schema as schema
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


@app.post('/add', response_model=schema.MachineAdd)
def add_new_machine(machine: schema.MachineAdd, db: Session = Depends(get_db)):
    machine_id = crud.get_machine_by_machine_id(db=db, machine_id=machine.machine_id)
    if machine_id:
        raise HTTPException(status_code=400, detail=f"Machine id {machine.machine_id} already exist in database: {machine_id}")
    return crud.add_machine_details_to_db(db=db, machine=machine)


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

@app.get('/machine-id')
def get_machine_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_machine_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.get_machine_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to get Machine: {e}")
    return crud.get_machine_by_id(db=db, sl_id=sl_id)