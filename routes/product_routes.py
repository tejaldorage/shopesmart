from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.product import Product
from database import get_db

router = APIRouter()

@router.post("/products/")
def create_product(product: Product, db: Session = Depends(get_db)):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product