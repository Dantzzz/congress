from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Member(Base):
    __tablename__ = 'member'
    bioguide_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    updated_at = Column(DateTime, nullable=True)