#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    """ WARNING: all classes who inherit from Base must be imported
    before calling Base.metadata.create_all(engine)"""
    Base.metadata.create_all(engine)
