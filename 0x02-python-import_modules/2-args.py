#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    numL = len(argv) - 1
    if numL <= 0:
        print("{} arguments.".format(numL))
    elif numL == 1:
        print("{} argument:".format(numL))
    else:
        print("{} arguments:".format(numL))
    for c in range(1, numL + 1):
        print("{}: {}".format(c, argv[c]))
