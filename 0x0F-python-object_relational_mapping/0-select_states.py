#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main():
    """This file uses a MySQL search from Python"""
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
# Database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states order by states.id")
    rows = cursor.fetchall()

    for states in rows:
        print(states)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
