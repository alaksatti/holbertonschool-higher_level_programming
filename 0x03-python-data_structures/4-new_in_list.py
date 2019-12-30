#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx is None or idx > (len(my_list) - 1) or idx < 0:
        return my_list
    if my_list is None:
        return None
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
