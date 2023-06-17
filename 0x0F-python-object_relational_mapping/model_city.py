#!/bin/usr/python3
'''creating cities schema.'''

from sqlalchemy import Column, Integer, String
from model_state import Base, State


class City(Base):
    '''instanciating class states.'''
    __tablename__ = 'cities'

    id = Column(Integer(), nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), nullable=False, ForeignKey=('State.id'))
