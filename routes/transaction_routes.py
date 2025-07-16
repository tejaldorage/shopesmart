from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.transaction import Transaction
from database import get_db

router = APIRouter()

@router.post("/transactions/")
def create_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction