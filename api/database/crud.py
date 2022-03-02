from sqlalchemy.orm import Session
import database.model as model
import database.schema as schema


def get_machine_by_machine_id(db: Session, machine_id: int):
    return db.query(model.Machine).filter(model.Machine.machine_id == machine_id).first()


def get_machine_by_id(db: Session, sl_id: int):
    return db.query(model.Machine).filter(model.Machine.id == sl_id).first()


def get_machine(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Machine).offset(skip).limit(limit).all()


def add_machine_details_to_db(db: Session, machine: schema.MachineAdd):
    machine_details = model.Machine(
        machine_id=machine.machine_id,
        machine_type=machine.machine_type,
        machine_number=machine.machine_number,
        machine_status=machine.machine_status,
        machine_grade=machine.machine_grade,
        machine_price=machine.machine_price
    )
    db.add(machine_details)
    db.commit()
    db.refresh(machine_details)
    return model.Machine(**machine.dict())


def update_machine_details(db: Session, sl_id: int, details: schema.UpdateMachine):
    db.query(model.Machine).filter(model.Machine.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Machine).filter(model.Machine.id == sl_id).first()

def update_price_machine_details(db: Session, sl_id: int, details: schema.UpdatePriceMachine):
    db.query(model.Machine).filter(model.Machine.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Machine).filter(model.Machine.id == sl_id).first()


def delete_machine_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Machine).filter(model.Machine.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)