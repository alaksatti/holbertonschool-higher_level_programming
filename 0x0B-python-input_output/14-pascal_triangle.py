#!/usr/bin/python3
"""
pascal_triangle module
"""


def pascal_triangle(n):
    """
    lis of lists of integers representing pascals's triangle
    """
    final = []
    for line in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = int(C * (line - i) / i)
        final.append(row)
    return final
