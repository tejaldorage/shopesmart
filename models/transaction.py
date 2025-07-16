from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base
from datetime import datetime

class Transaction(Base):
    _tablename_ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    purchase_date = Column(DateTime, default=datetime.utcnow)