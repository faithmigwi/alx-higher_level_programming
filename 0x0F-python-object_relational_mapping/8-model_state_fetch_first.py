#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


def fetch_all():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first_state = session.query(State).order_by(State.id).first()
    # HERE: no SQL query, only objects!
    if first_state is None:
        print('Nothing')
    print("{}: {}".format(first_state.id, first_state.name))
    session.close()


if __name__ == "__main__":
    fetch_all()
