#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a specified class"""
    return type(obj) is a_class
