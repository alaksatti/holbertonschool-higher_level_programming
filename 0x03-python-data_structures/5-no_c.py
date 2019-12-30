#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new = ''
    for c in my_string:
        if c not in ['C', 'c']:
            new += c
    return new
