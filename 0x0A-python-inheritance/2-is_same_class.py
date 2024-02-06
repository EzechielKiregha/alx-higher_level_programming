#!/usr/bin/python3
"""This module contains the is_same_class function"""


def is_same_class(obj, a_class):
    """Check if an object is of a certain class instance
    then True is return is yes, otherwise False
    """
    return (type(obj) is a_class)
