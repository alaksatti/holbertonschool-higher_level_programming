#!/usr/bin/python3
"""
append_after module
"""

def append_after(filename="", search_string="", new_string=""):
    """append a line of text to a file"""
    new_list = []
    with open(filename, "r", encoding="utf-8") as f:
        for lines in f:
            new_list.append(lines)

    with open(filename, "w", encoding="utf-8") as f:
        for lines in new_list:
            f.write(lines)
            if lines.find(search_string) != -1:
                f.write(new_string)
