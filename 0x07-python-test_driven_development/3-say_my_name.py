#!/usr/bin/python3
"""
prints first and last name
takes first name as argument
takes last name as argument
"""


def say_my_name(first_name, last_name=""):
    """
    prints first and last name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))
