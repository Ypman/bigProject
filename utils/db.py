# db.py

import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class ISO(Base):
    __tablename__ = 'iso'
    hakuna = Column(Integer, primary_key=True)
    matata = Column(Integer, primary_key=True)
    v1 = Column(Integer)
    v2 = Column(Integer)
    v3 = Column(Integer)
    province = Column(Integer)
    src = Column(Integer)
    country = Column(String(50), nullable=False)
    iso2 = Column(String(2))
    iso3 = Column(String(3))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine('sqlite:///sqlalchemy_test.db')

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)


def get_color_values(source_id):
    raise NotImplemented


def get_description():
    raise NotImplemented
