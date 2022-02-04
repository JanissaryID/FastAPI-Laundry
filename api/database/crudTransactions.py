from sqlalchemy.orm import Session
import database.model as model
import database.schemaTransactions as schema


def get_transactions_by_transactions_date(db: Session, transacrions_date: str):
    return db.query(model.TransactionsModel).filter(model.TransactionsModel.date == transacrions_date).first()


def get_transactions_by_date(db: Session, date: str):
    return db.query(model.TransactionsModel).filter(model.TransactionsModel.date == date).all()


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.TransactionsModel).offset(skip).limit(limit).all()


def add_transactions_details_to_db(db: Session, transactions: schema.TransactionsAdd):
    transactions_details = model.TransactionsModel(
        type=transactions.type,
        number=transactions.number,
        date=transactions.date,
        time=transactions.time,
        price=transactions.price
    )
    db.add(transactions_details)
    db.commit()
    db.refresh(transactions_details)
    return model.TransactionsModel(**transactions.dict())


# def update_machine_details(db: Session, sl_id: int, details: schema.UpdateMachine):
#     db.query(model.Machine).filter(model.Machine.id == sl_id).update(vars(details))
#     db.commit()
#     return db.query(model.Machine).filter(model.Machine.id == sl_id).first()


# def delete_machine_details_by_id(db: Session, sl_id: int):
#     try:
#         db.query(model.Machine).filter(model.Machine.id == sl_id).delete()
#         db.commit()
#     except Exception as e:
#         raise Exception(e)