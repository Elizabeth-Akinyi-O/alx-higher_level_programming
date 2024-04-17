#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, but is safe from MySQL injections!
"""

import MySQLdb
import sys


def main():
    """This file uses a MySQL search from Python"""
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
# Database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_password, db=db_name)
    cursor = db.cursor()
    fl_state_name = MySQLdb.escape_string(state_name).decode()
    sqlquery = ("SELECT * FROM states WHERE states.name='" +
                fl_state_name + "'")
    cursor.execute(sqlquery)
    rows = cursor.fetchall()

    for states in rows:
        print(states)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
