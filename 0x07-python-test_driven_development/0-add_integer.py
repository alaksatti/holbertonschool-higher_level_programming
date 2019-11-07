#!/usr/bin/python3


"""
Adds 2 integers together.
Args: ints/floats to be added.
Return:Sum of a and b.
"""


def add_integer(a, b=98):
    """
    Adds to integers together
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    total = (a + b)

    if abs(total) == float('inf'):
        raise OverflowError('overflow error')

    return (int(a) + int(b))
