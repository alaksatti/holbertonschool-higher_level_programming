#!/usr/bin/python3
"""Square class"""


class Square(__import__('9-rectangle').Rectangle):
    """
    class that inherits attributes from rectangle class
    """
    def __init__(self, size):
        """initializes attributes"""
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """returns a string that describes the square"""
        return '[Square] {}/{}'. format(self.__size, self.__size)
