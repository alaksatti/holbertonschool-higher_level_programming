#!/usr/bin/python3
""" takes in a URL and an email, sends a POST
request to the passed URL with the email as a
parameter, and displays the body of the response
(decoded in utf-8)
"""

from requests import post
from sys import argv

if __name__ == "__main__":
    fetched = post(argv[1], data={'email': argv[2]})
    print(fetched.text)
