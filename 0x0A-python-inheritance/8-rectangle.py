#!/usr/bin/python3
""" Rectangle class"""


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
