#!/usr/bin/python3
"""base geometry module"""


class BaseGeometry:
    """
    empty class
    """
    def area(self):
        """raise exception - area not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
