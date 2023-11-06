#!/usr/bin/python3
def helper(tuple_x=()):
    tuple_len = len(tuple_x)
    if tuple_len < 1:
        return (0, 0)
    elif tuple_len == 1:
        return (tuple_x[0], 0)
    else:
        return (tuple_x[0], tuple_x[1])


def add_tuple(tuple_a=(), tuple_b=()):
    a, b = helper(tuple_a)
    c, d = helper(tuple_b)

    return (a + c, b + d)
