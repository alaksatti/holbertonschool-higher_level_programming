#!/usr/bin/python3
def find_peak(list_of_integers):
    """ find peak in unsorted integers"""
    l = list_of_integers

    if l is None or len(l) == 0:
        return None

    elif l[0] > l[1]:
        return l[0]

    elif l[-1] > l[-2]:
        return l[-1]

    m = (len(l) - 1) // 2
    if l[m] < l[m - 1]:
            return find_peak(l[:m])

    if l[m] < l[m + 1]:
        return find_peak(l[m + 1:])

    return l[m]
