#!/usr/bin/python3
"""
(3-say_my name) module definition
This module supplies one function maned say_my_name
"""
def say_my_name(first_name, last_name=""):
    """Will print 'My name is' next up with first name and last name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}". format(first_name, last_name))
