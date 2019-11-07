#!/usr/bin/python3

"""
divides evevry element in matrix by div.
Returns: new list
takes matrix and div
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: divides every element in matrix by div.
    """
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) of int\
egers/floats')
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError('matrix must be a matrix (list of lists) of int\
egers/floats')
        for i in rows:
            if not isinstance(i, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of int\
egers/floats')

    for rows in matrix:
        if len(rows) == len(matrix[0]):
            pass
        else:
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return list(map(lambda l: list(map(lambda i: round(i/div, 2), l)), matrix))
