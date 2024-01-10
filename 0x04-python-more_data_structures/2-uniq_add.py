#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    for item in set(my_list):
        result += item
    return result
