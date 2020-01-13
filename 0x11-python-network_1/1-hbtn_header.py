#!/usr/bin/python3
""" figure out issue """
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as fetched:
        print(fetched.info()['X-Request-Id'])
