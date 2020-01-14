#!/usr/bin/python3
"""
Write a Python script that takes in a string and
sends a search request to the Star Wars API
"""
from requests import post
from requests import get
from sys import argv


if __name__ == "__main__":
    r = get('https://swapi.co/api/people', params={'search': argv[1]})
    if r.json() is None:
        print("Not a valid JSON")

    results = r.json().get('results')

    print("Number of results: {}".format(r.json().get('count')))
    tr = r.json()
    while(tr.get('next')):
        tr = get(tr.get('next')).json()
        results += tr.get('results')
    for e in results:
        print(e.get('name'))
        for film in e.get('films'):
            print("\t{}".format(get(film).json().get('title')))
