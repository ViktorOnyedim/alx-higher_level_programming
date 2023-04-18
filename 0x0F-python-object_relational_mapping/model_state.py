#!/usr/bin/python3
"""
Contains the class difinition of a 'State'
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

Base = declarative_base()
db = MySQLdb.connect(host="localhost", port=3306)


class State(Base):
    __tablename__ = states

    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
