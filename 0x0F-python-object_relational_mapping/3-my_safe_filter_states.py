#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, but is safe from MySQL injections!
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
# Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
# fl_state_name = MySQLdb.escape_string(state_name).decode()
    cursor.execute("SELECT * FROM states WHERE BINARY name=%s ORDER BY id",
                   (search, ))
    rows = cursor.fetchall()

    for states in rows:
        print(states)
    cursor.close()
    db.close()
