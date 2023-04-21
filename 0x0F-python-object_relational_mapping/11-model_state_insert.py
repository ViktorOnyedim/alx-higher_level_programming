#!/usr/bin/python3
"""Adds the 'State' object 'Louisiana' to the database 'hbtn_0e_6_usa'"""

from sys import argv, exit
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)

    """Create the connection to the database"""
    user, passwd, db_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db_name), pool_pre_ping=True)

    """Create the session and add a new state object"""
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    """Insert the new object into the database"""
    session.commit()

    print(new_state.id)

    session.close()
