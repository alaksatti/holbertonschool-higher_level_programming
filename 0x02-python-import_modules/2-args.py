#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = (len(sys.argv))

    if args == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    elif args == 1:
        print("0 arguments.")

    else:
        print("{} arguments:".format(args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, sys.argv[i]))
