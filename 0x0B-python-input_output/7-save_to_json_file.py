#!/usr/bin/python3
from json import dump
"""save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """writes an object to a txt file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        dump(my_obj, f)
