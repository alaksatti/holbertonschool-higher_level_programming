#!/usr/bin/python3

from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

data = urlencode({'email': argv[2]}).encode('utf-8')
with urlopen(argv[1], data) as fetched:
    print(fetched.read().decode('utf-8'))
