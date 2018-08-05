# db.py

import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()


class ISO(Base):
    __tablename__ = 'iso'
    hakuna = Column(Integer, primary_key=True, nullable=False)
    matata = Column(Integer, primary_key=True, nullable=False)
    v1 = Column(Integer)
    v2 = Column(Integer)
    v3 = Column(Integer)
    # province = Column(Integer)
    src = Column(Integer)
    # country = Column(String(50), nullable=False)
    iso2 = Column(String(2))
    # iso3 = Column(String(3))
    # timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    # def __repr__(self):
    #     return 'hakuna={}, matata={}, v1={}, v2={}, v3={}, p={}, src={}, is2={}, is3={}'\
    #         .format(self.hakuna, self.matata, self.v1, self.v2, self.v3, self.province, self.src, self.iso2, self.iso3)


engine = create_engine('sqlite:///sqlalchemy_test.db')

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


# Base.metadata.create_all(engine)
# user1 = session.query(ISO).filter_by(iso2="DE").first()
# print(user1)


# print(new_dict)


def get_color_values(source_id: int):
    result_dict = []
    if source_id == 999:
        for u in session.query(ISO).all():
            result_dict.append(u.__dict__)
    else:
        for u in session.query(ISO).filter_by(src=source_id).all():
            result_dict.append(u.__dict__)

    new_dict = {}
    for f in result_dict:
        if f['iso2'] not in new_dict:
            new_dict[f['iso2']] = {'v1': f['v1'], 'v2': f['v2'], 'v3': f['v3']}
            # print(new_dict[f['iso2']])
        if f['v1'] > new_dict[f['iso2']]['v1']:
            new_dict[f['iso2']]['v1'] = f['v1']
        elif f['v2'] > new_dict[f['iso2']]['v2']:
            new_dict[f['iso2']]['v2'] = f['v2']
        elif f['v3'] > new_dict[f['iso2']]['v3']:
            new_dict[f['iso2']]['v3'] = f['v3']

    return new_dict


def get_description():
    raise NotImplemented


print(get_color_values(95))
