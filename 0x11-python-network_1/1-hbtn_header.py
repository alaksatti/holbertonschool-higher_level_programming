#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."""
from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as fetched:
    print(fetched.info()['X-Request-Id'])
