#!/usr/bin/python3


def uppercase(str):

    for i in str:
        if i >= 'a' and i <= 'z':
            set = -32
        else:
            set = 0
        print("{:s}".format(chr(ord(i) + set)), end='')

    print()
