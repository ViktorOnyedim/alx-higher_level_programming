#!/usr/bin/python3
"""
Lists all 'State' objects that contain the letter 'a'
from the database 'hbtn_0e_6_usa'
"""

from sys import argv, exit
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

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

    query = session.query(State)
    filter_condition = (State.name.like('%a%'))
    states_a = query.filter(filter_condition).order_by(State.id.asc()).all()

    for state in states_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
