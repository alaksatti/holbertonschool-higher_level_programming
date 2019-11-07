#!/usr/bin/python3
"""Class student
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        """ initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves dictionary representation of student"""
        return self.__dict__
