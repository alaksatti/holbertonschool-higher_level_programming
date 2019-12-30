#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for e in rows:
            if e != rows[-1]:
                print("{:d}".format(e), end=' ')
            else:
                print("{:d}".format(e), end='')
        print()
