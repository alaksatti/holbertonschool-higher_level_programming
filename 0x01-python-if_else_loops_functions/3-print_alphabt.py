#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if i in [ord('q'), ord('e')]:
        continue
    else:
        print("{:s}".format(chr(i)), end="")
