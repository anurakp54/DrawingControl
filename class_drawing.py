from sqlalchemy import Column, String, Integer, Date
from base import Base
from _datetime import datetime


class drawing(Base):
    __tablename__ = 'drawing'

    id = Column(Integer, primary_key=True)
    dwg_num = Column(String(12))
    created = Column(Date, default=datetime.utcnow())

    def __init__(self, dwg_num):
        self.dwg_num = dwg_num

    def __repr__(self):
        return f'<drawing: {self.dwg_num}>'
