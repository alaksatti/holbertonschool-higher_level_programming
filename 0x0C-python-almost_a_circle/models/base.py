#!/usr/bin/python3
"""base module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """object to json str"""
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json repr of object to file"""
        with open(cls.__name__ + '.json', "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")

            else:
                f.write(cls.to_json_string(
                    [o.to_dictionary() for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """json str to object"""
        if not isinstance(json_string, str) or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)

        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances from a file"""
        obj_list = []

        try:
            with open(cls.__name__ + '.json', "r", encoding='utf-8') as f:
                txtfile = f.read()

            for objects in cls.from_json_string(txtfile):
                obj_list.append(cls.create(**objects))

        except:
            pass

        return obj_list
