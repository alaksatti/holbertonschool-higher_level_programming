#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """update square"""
        attributes = ['id', 'size', 'x', 'y']

        if args and 0 < len(args) < 5:
            for i, value in enumerate(args):
                if i == 0:
                    super().update(value)
                else:
                    self.__setattr__(attributes[i], value)
        elif kwargs and 0 < len(kwargs) < 5:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == 'id':
                        super().update(id=value)
                    else:
                        self.__setattr__(key, value)

    def to_dictionary(self):
        """dictionary representation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
