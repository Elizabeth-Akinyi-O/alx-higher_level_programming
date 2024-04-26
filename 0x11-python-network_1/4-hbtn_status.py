#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """

import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    txt = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(txt), txt))
