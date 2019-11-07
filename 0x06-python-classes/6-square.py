#!/usr/bin/python3


class Square:
    """class Square defines a square by size"""
    def __init__(self, size=0, position=(0, 0)):
        "initialize"
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """return square of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        if not self.__size:
            print("")

        else:
            for i in range(self.__position[1]):
                print("")

            for i in range(0, self.__size):
                for k in range(0, self.position[0]):
                    print(' ', end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print("")
