#!/usr/bin/python3
def element_at(my_list, idx):
    num_el = 0
    if my_list is not None:
        num_el = len(my_list)
    if idx < 0 or idx >= num_el or num_el == 0:
        return None
    return my_list[idx]
