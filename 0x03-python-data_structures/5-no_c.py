#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    no_clist = ""
    for a in range(len(my_string)):
        if my_string[a] == 'c' or my_string[a] == 'C':
            continue
        no_clist += my_string[a]
    return no_clist
