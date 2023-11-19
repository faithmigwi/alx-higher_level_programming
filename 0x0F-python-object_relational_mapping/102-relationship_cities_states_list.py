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
    Your script should connect to a MySQL server
    running on localhost at port 3306.
    You must use only one query to the database.
    You must use the state relationship to access to
    the State object linked to the City object.
    Results must be sorted in ascending order by cities.id.
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

    rows = session.query(City).order_by(City.id).all()
    for from_city in rows:
        print("{}: {} -> {}".format(from_city.id,
                                    from_city.name, from_city.state.name))

    session.close()


if __name__ == "__main__":
    fetch_all()
