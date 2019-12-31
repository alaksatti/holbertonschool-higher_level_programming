#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 != 0:
        off = -32
    else:
        off = 0
        
    print(chr(i + off), end='')
