#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the body
of the response.

If the HTTP status code is greater than or equal to 400, print:
     Error code: followed by the value of the HTTP status code
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    ERR_TXT = 'Error code: {}'
    status = response.status_code
    print(ERR_TXT.format(status) if (status >= 400) else response.text)
