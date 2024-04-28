#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    tble = "states"
# Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM {} WHERE BINARY name='{}' ORDER BY id"
                   .format(tble, search))

    rows = cursor.fetchall()

    for states in rows:
        print(states)

    cursor.close()
    db.close()
