#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
 and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_it():
    """
    script thats is safe from MYSQL Injections
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    state_searched = sys.argv[4]
    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities LEFT JOIN states ON "
                "states.id = cities.state_id WHERE states.name = %s "
                "ORDER BY cities.id ASC;", (state_searched,))
    result = cur.fetchall()
    cur.close()
    db.close()

    print(", ".join([row[0] for row in result]))


if __name__ == '__main__':
    list_it()
