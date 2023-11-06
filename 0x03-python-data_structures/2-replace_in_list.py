#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num_el = 0
    if my_list is not None:
        num_el = len(my_list)
    if idx < 0 or idx >= num_el or num_el == 0:
        return my_list
    my_list[idx] = element
    return my_list
