#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

Script takes 4 arguments: mysql username
                          mysql password
                          database name
                          state name (SQL injection free!)


"""

import MySQLdb
from sys import argv
import re


if __name__ == "__main__":
    # error handling for missing args
    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    state_name = ' '.join(argv[4].split())
# Use the re search func to search for a state name match of the regex pattern
    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('Enter a valid state name (example: Arizona)')
        exit(1)

# Database connection
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
        )
# error handling for Database connection
    except Exception:
        print('Failed to connect to Database')
        exit(0)

    cursor = db.cursor()
    data = cursor.execute("SELECT cities.name FROM cities" +
                          " JOIN states" +
                          " ON cities.state_id = states.id" +
                          " WHERE states.name = '{:s}'".format(state_name))
    rows = cursor.fetchall()

    processed_data = []

    for a in range(data):
        processed_data.append(rows[a][0])

    print(', '.join(processed_data))

    cursor.close()
    db.close()
