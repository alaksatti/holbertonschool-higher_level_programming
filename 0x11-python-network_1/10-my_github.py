#!/usr/bin/python3
"""
Takes your Github credentials (username and password)
and uses the Github API to display your id
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if r.json():
        print(r.json().get('id'))
    else:
        print("Not a valid JSON")
