#!/usr/bin/python3
"""
Python file similar to model_state.py named
model_city.py that contains the class definition of a City
"""

import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


def fetch_all():
    """
    Your script should take 3 arguments: mysql username,
    mysql password and database name.
    You must use the module SQLAlchemy.
    The connection to your MySQL server must be to localhost on port 3306.
    You must only use one query to the database.
    You must use the cities relationship for all State objects.
    Results must be sorted in ascending order by states.id and cities.id.
    Results must be displayed as they are in the example below.
    Your code should not be executed when imported.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).order_by(State.id).all()
    for state_row in rows:
        print("{}: {}".format(state_row.id, state_row.name))
        for city_row in state_row.cities:
            print("    {}: {}".format(city_row.id, city_row.name))
    session.close()


if __name__ == "__main__":
    fetch_all()
