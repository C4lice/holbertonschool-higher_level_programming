#!/usr/bin/python3
"""
module that define a table with sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class that represente the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(128))
