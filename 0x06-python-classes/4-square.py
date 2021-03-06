#!/usr/bin/python3


class Square:
    """class Square defines a square by size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """return square of a square"""
        return self.__size ** 2
