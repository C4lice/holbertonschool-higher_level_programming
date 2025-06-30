#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy.orm.exc import NoResultFound


def main():
    """
    fonction use to search good data
    """
    session = sessionmaker(engine)
    session = session()
    try:
        for state in session.query(State).order_by(State.id).all():
            if 'a' in state.name:
                print("{}: {}".format(state.id, state.name))
    except NoResultFound:
        print("Nothing")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    main()
