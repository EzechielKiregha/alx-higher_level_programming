#!/usr/bin/python3
"""
this module supply the inherits_from function
"""



def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
