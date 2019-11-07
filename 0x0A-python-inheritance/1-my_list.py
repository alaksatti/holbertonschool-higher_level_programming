#!/usr/bin/python3
"""Mylist class"""


class MyList(list):
    """
    inherits from list print_sorted function
    """
    def print_sorted(self):
        """ prints list in ascended sorted order"""
        print(sorted(self))
