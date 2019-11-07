#!/usr/bin/python3

"""
prints a sqaure with '#' character.
Size: size length of square.
Returns: a printed square.
"""


def print_square(size):
    """
    prints a square with '#'.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
