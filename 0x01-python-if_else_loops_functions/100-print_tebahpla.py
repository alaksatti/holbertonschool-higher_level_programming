#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 != 0:
        print(chr(i - 32), end='')
    else:
        print(chr(i), end='')
