#!/usr/bin/python3
""" figure out issue """
from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as fetched:
    print(fetched.info()['X-Request-Id'])
