# db.py

import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships
from sqlalchemy import create_engine

Base = declarative_base()


class ISO(Base):
    __tablename__ = 'iso'
    mcc = Column(Integer, primary_key=True)
    mnc = Column(Integer, primary_key=True)
    v1 = Column(Integer, nullable=False)
    v2 = Column(Integer, nullable=False)
    v3 = Column(Integer, nullable=False)
    prov = Column(Integer)
    src = Column(Integer)
    country = Column(String(2), nullable=False)
    iso2 = Column(String(20))
    iso3 = Column(String(20))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine('sqlite:///sqlalchemy_test.db')

Base.metadata.create_all(engine)
