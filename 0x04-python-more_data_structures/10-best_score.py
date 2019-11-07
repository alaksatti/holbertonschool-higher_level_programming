#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = None
    maxkey = None

    for keys, values in a_dictionary.items():
        if not max or values > max:
            max = values
            maxkey = keys
    return maxkey
