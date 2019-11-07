#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """returns whether is an instance of an inherited class"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
