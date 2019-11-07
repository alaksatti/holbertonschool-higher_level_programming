#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0

    total = sum(map(lambda i: i[1], my_list))
    weighted = sum(map(lambda x: x[0] * x[1], my_list))
    return weighted / total
