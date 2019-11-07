#!/usr/bin/python3
from json import loads
"""from_json_string"""


def from_json_string(my_str):
    """converts JSON string to python object"""
    return loads(my_str)
