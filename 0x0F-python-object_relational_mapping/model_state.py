#!/usr/bin/python3
"""
    contains the class definition of a\
        State and an instance Base = declarative_base():
"""


import sqlalchemy
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State Representation"""

    __tablename__ = 'states'

    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
