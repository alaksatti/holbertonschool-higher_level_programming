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

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of student"""
        dict_attr = {}
        if type(attrs) is list and attrs is not None:
            if all(isinstance(elem, str) for elem in attrs):
                for k, v in self.__dict__.items():
                    if k in attrs:
                        dict_attr[k] = self.__dict__[k]
            else:
                return self.__dict__
        else:
            return self.__dict__
        return dict_attr
