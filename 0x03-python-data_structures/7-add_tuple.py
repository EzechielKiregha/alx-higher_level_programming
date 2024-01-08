#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_length_a = len(tuple_a)
    tuple_length_b = len(tuple_b)

    if tuple_length_a < 1:
        tuple_a = (0, 0)
    elif tuple_length_a < 2:
        tuple_a = (tuple_a[0], 0)

    # check for tuple_b
    if tuple_length_b < 1:
        tuple_b = (0, 0)
    elif tuple_length_b < 2:
        tuple_b = (tuple_b[0], 0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
