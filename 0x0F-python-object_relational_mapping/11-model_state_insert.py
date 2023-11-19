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

    inserting = State(name="Louisiana")

    session.add(inserting)

    new_state = session.query(State).filter(State.name == 'Louisiana')\
        .order_by(State.id).first()

    session.commit()

    print("{}".format(new_state.id))

    session.close()


if __name__ == "__main__":
    fetch_all()
