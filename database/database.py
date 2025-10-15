from sqlalchemy import Column, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Analyst(Base):
    __tablename__ = "analysts"
    pass