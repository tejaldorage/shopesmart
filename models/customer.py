from sqlalchemy import Column, Integer, String
from database import Base

class Customer(Base):
    _tablename_ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)