from sqlalchemy import Column, Integer, Date
from .base import Base

class Congress(Base):
    __tablename__ = 'congress'
    congress_number = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)