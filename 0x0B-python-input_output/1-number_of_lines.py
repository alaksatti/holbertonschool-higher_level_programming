#!/usr/bin/python3
"""number_of_lines module"""


def number_of_lines(filename=""):
    """returns number of lines in a textfile"""
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for line in f)
