# from app import db

# class Event(db.Model):
#     _id = db.Column(db.Integer, primary_key=True)
#     author = db.Column(db.String(100), unique=False, nullable=False)
#     from_date = db.Column(db.Date, unique=False, nullable=False)
#     to_date = db.Column(db.Date, unique=False, nullable=False)
#     theme = db.Column(db.String(80), unique=False, nullable=False)
#     description = db.Column(db.String(500), unique=False, nullable=False)

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
metadata = Base.metadata

class Event(Base):
    __tablename__ = 'event'
    _id = Column(Integer, primary_key=True)
    author = Column(String(100), unique=False, nullable=False)
    from_date = Column(Date, unique=False, nullable=False)
    to_date = Column(Date, unique=False, nullable=False)
    theme = Column(String(80), unique=False, nullable=False)
    description = Column(String(500), unique=False, nullable=False)