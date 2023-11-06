#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    num_el = len(my_list)
    if idx < 0 or idx >= num_el or num_el == 0:
        return my_list[:]
    temp_list = my_list[:]
    temp_list[idx] = element
    return temp_list
