#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen

with urlopen("https://intranet.hbtn.io/status") as fetched:
    r = fetched.read()
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode('utf-8')))
