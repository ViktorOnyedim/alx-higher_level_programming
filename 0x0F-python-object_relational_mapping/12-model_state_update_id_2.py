#!/usr/bin/python3
"""Changes the name of a 'State' object from the database 'hbtn_0e_6_usa"""

from sys import argv, exit
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)

    user, passwd, db_name = argv[1], argv[2], argv[3]
    """Create a database connection"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).all()
    for state in states:
        state.name = "New Mexico"

    session.close()
