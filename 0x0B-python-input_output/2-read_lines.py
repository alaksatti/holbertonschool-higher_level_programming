#!/usr/bin/python3
"""read_n_lines module"""


def read_lines(filename="", nb_lines=0):
    """reads nb_lines number of lines"""
    with open(filename, "r", encoding="utf-8") as f:
        for lines in f:
            print(lines, end='')
            nb_lines -= 1

            if not nb_lines:
                break
