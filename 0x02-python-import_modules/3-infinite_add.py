#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sums = 0
    for i in range(1, len(argv)):
        sums += int(argv[i])
    print(sums)
