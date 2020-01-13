#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    req = post('http://0.0.0.0:5000/search_user', data={'q': q})
    if 'json' not in req.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if req.json():
            r = req.json()
            print("[{}] {}".format(r['id'], r['name']))
        else:
             print("No result")
