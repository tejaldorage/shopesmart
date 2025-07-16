from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    _tablename_ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)