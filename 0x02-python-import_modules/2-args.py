#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv)
    if args == 2:
        print("{0:d} argument:".format(args - 1))
    elif args == 1:
        print("{0:d} arguments.".format(args - 1))
    else:
        print("{0:d} arguments:".format(args - 1))
    for i in range(1, args):
        print("{0:d}: {1:s}".format(i, sys.argv[i]))
