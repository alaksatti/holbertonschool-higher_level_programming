#!/usr/bin/python3


"""
text_indentation prints 2 new lines after '.', '?', and ':'.
Args: text.
Return: Nothing:
"""


def text_indentation(text):
    """
    prints 2 new lines after '.', '?', and ':'.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for char in ['?', ':', '.']:
        text = text.replace(char, char + "\n\n")

    print("\n".join(i.strip() for i in text.split('\n')), end='')
