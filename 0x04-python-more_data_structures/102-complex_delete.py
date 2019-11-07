#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = []

    for key, values in a_dictionary.items():
        if value is values:
            new_dic.append(key)

    for key in new_dic:
        del a_dictionary[key]
    return a_dictionary
