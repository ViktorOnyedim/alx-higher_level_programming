#!/usr/bin/python3
"""Prints the first 'State' object from the database 'hbtn_0e_6_usa'"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv, exit
from model_state import Base, State

if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)

    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
