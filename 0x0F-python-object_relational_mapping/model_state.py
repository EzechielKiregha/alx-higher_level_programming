#!/usr/bin/python3
"""
a module that holds the State class
and an instance of the declarative orm mapper
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
