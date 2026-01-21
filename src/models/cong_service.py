from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .base import Base

class CongService(Base):
    __tablename__ = 'cong_service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bioguide_id = Column(String, ForeignKey('member.bioguide_id'), nullable=False)
    congress_number = Column(Integer, ForeignKey('congress.congress_number'), nullable=False)
    chamber = Column(String, nullable=False)
    district = Column(Integer, nullable=True)
    party = Column(String, nullable=False)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)