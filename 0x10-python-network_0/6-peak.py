#!/usr/bin/python3
def find_peak(list_of_integers):
    """ find peak in unsorted integers"""
    l = list_of_integers

    if l is None or len(l) == 0:
        return None

    if l[0] > l[1]:
        return l[0]

    if l[-1] > l[-2]:
        return l[-1]

    for x in range(1, (len(l) - 1)):
        if l[x] > l[x - 1]:
            if l[x] > l[x + 1]:
                return l[x]
    return l[1]
