#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""

from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as fetched:
            print(fetched.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))
