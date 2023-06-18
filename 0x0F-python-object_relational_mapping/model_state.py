#!/bin/usr/python3
'''Defines a state model'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''instanciating class states.'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
