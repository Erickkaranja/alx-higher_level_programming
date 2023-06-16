#!/usr/bin/python3
'''script that lists all State objects from the database.
   using MySQLalchemy.
   usage: ./7-model_state_fetch_all.py host passwd database.
'''
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)
import sys
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
                           .format(sys.argv[1],\
                           sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(states.id))
            found = True
    if found is False:
        print("Not found")
