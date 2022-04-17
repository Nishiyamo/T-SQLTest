from sqlalchemy import Column, String, Float, Date
from import

Base = declarative_base()

class Customer(EqMixin, Base):
    __tablename__ = "Customer"
    CustomerId = db.Column()
