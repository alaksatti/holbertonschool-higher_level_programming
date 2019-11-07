#!/usr/bin/python3

"""
LockedClass prevents the user from dynamically creating new instance attribute.
new instance attribute first name allowed.

"""


class LockedClass:
    """
    no class object/class attribute except first_name
    """
    __slots__ = 'first_name'

    def __init__(self):
        pass
