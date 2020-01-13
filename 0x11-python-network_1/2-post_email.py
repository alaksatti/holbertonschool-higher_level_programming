#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

data = urlencode({'email': argv[2]}).encode('utf-8')
with urlopen(argv[1], data) as fetched:
    print(fetched.read().decode('utf-8'))