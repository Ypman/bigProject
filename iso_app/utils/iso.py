# iso.py

from iso_app import db


class ISO(db.Model):
    # __tablename__ = 'iso'
    hakuna = db.Column(db.Integer, primary_key=True, nullable=False)
    matata = db.Column(db.Integer, primary_key=True, nullable=False)
    v1 = db.Column(db.Integer)
    v2 = db.Column(db.Integer)
    v3 = db.Column(db.Integer)
    src = db.Column(db.Integer)
    iso2 = db.Column(db.String(2))
    province = db.Column(db.String(100))
    timestamp = db.column(db.Integer)
