#!/usr/bin/python3
"""Function that adds new attribute to an object"""


def add_attribute(obj, attribute, value):
    """Adds to attribute to an object if its possible"""
    if isinstance(obj, (float, bool, int, str, tuple, range, bytes, complex,
                        frozenset)):
            raise TypeError("can't add new attribute")

    obj.__setattr__(attribute, value)
