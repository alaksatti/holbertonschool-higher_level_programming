#!/usr/bin/python3

"""
Class rectangle: defines a rectangle.
Defines height and width.

"""


class Rectangle:
    """
    class square with width and height
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def perimeter(self):
        """ area of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2 + self.width * 2)

    def area(self):
        """perimeter of rectangle """
        return (self.height * self.width)
