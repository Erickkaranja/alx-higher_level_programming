#!/usr/bin/python3
'''Adding a new state'''
from model_state import Base, State
import sys
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
                           .format(sys.argv[1], sys.argv[2],\
                           sys.argv[3]), pool_pre_ping=True)
    newval = engine.execute("INSERT INTO `sys.argv[3]`.`State` (`name`) VALUE\
                            ('Louisiana')")
