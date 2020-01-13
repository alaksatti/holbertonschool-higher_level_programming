#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status"""
from requests import get

r = get("https://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r))
print("\t- utf8 content: {}".format(r.decode('utf-8')))
