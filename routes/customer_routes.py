from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.customer import Customer
from database import get_db

router = APIRouter()

@router.post("/customers/")
def create_customer(customer: Customer, db: Session = Depends(get_db)):
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer