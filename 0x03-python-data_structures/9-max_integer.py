#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 1:
        return None
    max_val = my_list[0]
    for a in range(len(my_list)):
        if max_val < my_list[a]:
            max_val = my_list[a]
    return max_val
