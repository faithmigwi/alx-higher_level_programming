#!/usr/bin/python3
""" script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_it():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}'"
                " ORDER BY id ASC".format(state_searched))
    result = cur.fetchall()
    cur.close()
    db.close()
    for row in result:
        if row[1] == state_searched:
            print(row)


if __name__ == '__main__':
    list_it()
