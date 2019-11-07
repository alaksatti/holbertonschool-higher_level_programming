#!/usr/bin/python3


def remove_char_at(str, n):
    newstr = ''

    for c in str:
        if n != 0:
            newstr += c
        n -= 1

    return (newstr)
