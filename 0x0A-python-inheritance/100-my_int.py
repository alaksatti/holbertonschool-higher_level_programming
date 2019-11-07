#!/usr/bin/python3
"""Myint module"""


class MyInt(int):
    """
    class inherited from int
    """
    def __eq__(self, other):
        """Checks if equal"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """checks if equal"""
        return not super().__ne__(other)
