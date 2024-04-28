#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    URL = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    payload = {}
    payload['q'] = q
    response = requests.post(url=url, data=payload)

    try:
        parsed_json = response.json()
        if parsed_json:
            print("[{}] {}".format(parsed_json.get("id"),
                                   parsed_json.get("name")))
        else:
            print('No result')
    except Exception as error:
        print('Not a valid JSON')
