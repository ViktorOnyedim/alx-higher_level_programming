#!/usr/bin/python3
"""
Deletes all 'State' objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa'
"""

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

    try:
        states_a = session.query(State).filter(State.name.like('%a%')).all()
        for state in states_a:
            session.delete(state)

        """Save changes to database"""
        session.commit()
    except Exception as e:
        print("Error: {}".format(e))
        session.rollback()
    finally:
        session.close()
