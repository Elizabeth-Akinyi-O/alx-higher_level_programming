#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


def main():
    """This file uses a mysql search from python"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
# Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    sqlquery = ("""SELECT cities.id, cities.name, states.name FROM states JOIN
                cities ON states.id=cities.state_id ORDER BY cities.id ASC""")
    cursor.execute(sqlquery)
    rows = cursor.fetchall()

    for states in rows:
        print(states)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
