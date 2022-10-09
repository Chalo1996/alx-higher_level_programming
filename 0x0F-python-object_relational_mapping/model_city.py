#!/usr/bin/python3
"""contains the class definition of a City
"""


import sqlalchemy
from sqlalchemy import (
    Integer, String, Column, ForeignKey
)
from model_state import Base, State


class City(Base):
    """Representation of the City Object"""
    __tablename__ = 'cities'

    id = Column(Integer(), unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        """Instantiate city.name"""
        self.name = name
