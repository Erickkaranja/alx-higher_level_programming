#!/usr/bin/python3
'''script that changes the name of a State object from the database.'''

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    row = State(value='Louisiana')
    session.add()
    session.commit()
