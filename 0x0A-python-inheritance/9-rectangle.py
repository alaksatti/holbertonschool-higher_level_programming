#!/usr/bin/python3
"""Rectangle class"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """
    class that inherits attributes from BaseGeometry
    """
    def __init__(self, width, height):
        """initializes attributes"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string that describes the rectangle"""
        return '[Rectangle] {}/{}'. format(self.__width, self.__height)
