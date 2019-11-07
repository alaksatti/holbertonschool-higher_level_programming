#!/usr/bin/python3
from json import load
"""load_from_json_file"""


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, "r") as f:
        return load(f)
