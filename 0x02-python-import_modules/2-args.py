#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) not in [1, 2]:
        print((str(len(argv) - 1)) + " arguments:")
    elif len(argv) == 1:
        print("0 arguments.")
    else:
        print("1 argument:")
    for i in range(1, len(argv)):
        print(str(i) + ": {}".format(argv[i])) 
