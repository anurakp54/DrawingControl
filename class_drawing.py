from DateTime import DateTime
from sqlalchemy import Column, String, Integer, DateTime, Date
from base import Base
from _datetime import datetime


class drawing(Base):
    __tablename__ = 'drawing'

    id = Column(Integer, primary_key=True)
    dwg_num = Column(String(12))
    revision= Column(String(2))
    created = Column(DateTime, default=datetime.utcnow())

    def __init__(self, dwg_num, revision, created):
        self.dwg_num = dwg_num
        self.revision = revision
        self.created = created

    def __repr__(self):
        return f'<drawing: {self.dwg_num}{self.revision} created {self.created}>'
