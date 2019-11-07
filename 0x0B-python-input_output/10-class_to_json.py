#!/usr/bin/python3
"""class to json module
"""


def class_to_json(obj):
    """returns the dictionary description for JSON sterilization of an oject
    """
    return obj.__dict__
