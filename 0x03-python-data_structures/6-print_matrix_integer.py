#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for lists in matrix:
        for element in lists:
            print("{:d}".format(element), end='')
            if element != lists[-1]:
                print("".format(), end=' ')
        print()
