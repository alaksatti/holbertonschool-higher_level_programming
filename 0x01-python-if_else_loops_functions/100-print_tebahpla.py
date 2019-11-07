#!/usr/bin/python3

for i in reversed(range(ord('a'), ord('z') + 1)):
    if (i % 2 == 0):
        set = 0
    else:
        set = -32

    print("{:s}".format(chr(i + set)), end='')
