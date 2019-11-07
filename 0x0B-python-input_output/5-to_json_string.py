#!/usr/bin/python3
from json import dumps
"""To JSON string module"""


def to_json_string(my_obj):
    """returns JSON string representation of an object"""
    return dumps(my_obj)
