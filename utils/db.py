# db.py

import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class ISO(Base):
    __tablename__ = 'iso'
    hakuna = Column(Integer, primary_key=True, nullable=False)
    matata = Column(Integer, primary_key=True, nullable=False)
    v1 = Column(Integer)
    v2 = Column(Integer)
    v3 = Column(Integer)
    province = Column(Integer)
    src = Column(Integer)
    country = Column(String(50), nullable=False)
    iso2 = Column(String(2))
    iso3 = Column(String(3))
    # timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return 'hakuna={}, matata={}, v1={}, v2={}, v3={}, p={}, src={}, is2={}, is3={}'\
            .format(self.hakuna, self.matata, self.v1, self.v2, self.v3, self.province, self.src, self.iso2, self.iso3)


engine = create_engine('sqlite:///sqlalchemy_test.db')

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Base.metadata.create_all(engine)
user1 = session.query(ISO).filter_by(iso2="DE").first()
print(user1)


def get_color_values(source_id):
    raise NotImplemented


def get_description():
    raise NotImplemented
