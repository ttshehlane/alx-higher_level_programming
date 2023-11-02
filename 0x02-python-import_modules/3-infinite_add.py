#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    if len(argv) == 1:
        print("0")
    else:
        for c in range(1, len(argv)):
            sum += int(argv[c])
    print("{}".format(sum))
