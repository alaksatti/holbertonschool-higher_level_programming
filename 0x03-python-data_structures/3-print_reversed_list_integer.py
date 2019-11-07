#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        return None

    length = len(my_list)

    if length:
        for i in reversed(range(0, length)):
            print("{:d}".format(my_list[i]))
