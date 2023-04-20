from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''Declaring class state that inherits from Base model.

    Attributes:
        __tablename__ (str): name of mysql table to be created to represent
               class state.
        id (int) : unique id that acts as the primary key.
        name(str): represents the name column of class state.
    '''
    __tablename__="states"
    name = Column(String(128), nullable=False)
    id = Column(Integer, autoincrement=True, primary_key=True)
