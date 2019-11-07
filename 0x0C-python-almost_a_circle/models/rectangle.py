#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns area"""
        return self.width * self.height

    def display(self):
        """display"""
        for lines in range(self.y):
            print()
        for lines in range(self.height):
            print('{}{}'.format(' ' * self.x, '#' * self.width))

    def __str__(self):
        """print str representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update"""
        attribute = ['id', 'width', 'height', 'x', 'y']

        if args and 0 < len(args) <= 5:
            for i, value in enumerate(args):
                if i == 0:
                    super().__init__(value)
                else:
                    self.__setattr__(attribute[i], value)

        elif kwargs and 0 < len(kwargs) <= 5:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                elif key in attribute:
                    self.__setattr__(key, value)

    def to_dictionary(self):
        """dictionary representation"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x':
                self.x, 'y': self.y}
