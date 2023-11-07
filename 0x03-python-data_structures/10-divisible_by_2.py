#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) < 1:
        return None
    temp = []
    for a in range(len(my_list)):
        if (my_list[a] % 2) == 0:
            temp.append(True)
        else:
            temp.append(False)
    return temp
