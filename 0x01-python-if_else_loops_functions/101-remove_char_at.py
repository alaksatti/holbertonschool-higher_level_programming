#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ''
    for i in range(0, len(str)):
        if i != n:
            new_string += str[i]
    return new_string
