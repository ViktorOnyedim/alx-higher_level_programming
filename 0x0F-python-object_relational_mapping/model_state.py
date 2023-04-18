#!/usr/bin/python3
"""
Contains the class difinition of a 'State'
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Defines a State class

    Attributes:
        __tablename__ (str): Table name of the class
        id (int): State id of the class
        name (str): State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
