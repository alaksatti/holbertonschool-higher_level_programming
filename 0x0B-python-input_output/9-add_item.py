#!/usr/bin/python3
from sys import argv
load_f = __import__('8-load_from_json_file').load_from_json_file
save_f = __import__('7-save_to_json_file').save_to_json_file

"""add_item module"""


if __name__ == '__main__':
    try:
        py_list = load_f("add_item.json")

    except:
        py_list = []

    for i in range(1, len(argv)):
        py_list.append(argv[i])

    save_f(py_list, "add_item.json")
