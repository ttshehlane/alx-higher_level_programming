#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        for a in range(0, len(my_list)):
            print("{:d}".format(my_list[a]))
