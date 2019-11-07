#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    i, j = 0, 0

    if len_a > 0:
        i += tuple_a[0]
    if len_a > 1:
        j += tuple_a[1]
    if len_b > 0:
        i += tuple_b[0]
    if len_b > 1:
        j += tuple_b[1]
    return i, j
