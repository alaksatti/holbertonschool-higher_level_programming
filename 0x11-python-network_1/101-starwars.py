#!/usr/bin/python3
"""
Write a Python script that takes in a string and
sends a search request to the Star Wars API
"""
from requests import post
from requests import get
from sys import argv

if __name__ == "__main__":
    r = post('https://swapi.co/api/people', params={'search': argv[1]})
    if r.json():
        print("Number of results: {}".format(r.json()['count']))
        for user in r.json()['results']:
            print(user['name'])
        tr = r.json()
        while (tr['next']):
            tr = get(r.json()['next']).json()
            for user in tr['results']:
                print(user['name'])
    else:
        print('Not a valid JSON')
