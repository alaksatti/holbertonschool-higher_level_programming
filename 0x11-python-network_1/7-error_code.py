#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
If the HTTP status code is greater than or equal to 400
print: Error code: followed by the value of the HTTP status code
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    fetched = get(argv[1])

    if fetched.status_code < 400:
        print(fetched.text)
    else:
        print('Error code: {}'.format(fetched.status_code))
