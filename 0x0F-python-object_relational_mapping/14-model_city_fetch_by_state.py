#!/usr/bin/python3
"""Prints all 'City' objects from the database 'hbtn_0e_14_usa'"""

from sys import argv, exit
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)

    user, passwd, db_name = argv[1], argv[2], argv[3]
    """Create a database connection"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """Create a session to interact with database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State.name)
    """Join State table with the City table"""
    join_condition = (City.state_id == State.id)

    cities = query.join(State, join_condition).order_by(City.id.asc()).all()

    for city, state_name in cities:
        print("{}: {} {}".format(state_name, city.id, city.name))

    session.close()
