import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


url = 'postgresql://postgres:123456@localhost/postgres'
engine = sqlalchemy.create_engine(url)
session = Session(engine)
Base = declarative_base()