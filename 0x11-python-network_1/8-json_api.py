#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(URL, data)

    cont_type = response.headers['content-type']

    if cont_type == 'application/json':
        result = response.json()
        user_id = result.get('id')
        user_name = result.get('name')
        if (result != {} and user_id and user_name):
            print("[{}] {}".format(user_id, user_name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
