#!/usr/bin/python3
"""Contains the class definition of 'City'"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Defines a State class

    Attributes:
        __tablename__ (str): Table name of the class
        id (int): City id of the class
        name (str): City name of the class
    """

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
