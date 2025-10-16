from typing import Type

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine


class DatabaseWorker:
    def __init__(self, table: Type[DeclarativeBase], database_url: str):
        database_url = database_url
        engine = create_engine(database_url)
        self.__table = table
        self.__session = sessionmaker(bind=engine)()

    @property
    def table(self):
        return self.__table

    @property
    def session(self):
        return self.__session