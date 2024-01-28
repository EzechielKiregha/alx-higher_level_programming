#!/usr/bin/python3
"""This module provides a function to add two numbers.

The add_integer function can take two arguments, a and b, which can be either integers or floats.
It adds these two numbers together and returns the result. If either a or b is a float, it is
converted to an integer before the addition.

Example:
        >>> add_integer(3, 5)
        8
"""


def add_integer(a, b=98):
    """Adds two numbers and returns the result.

       This function takes two arguments, `a` and `b`, which can be integers or floats.
       If either `a` or `b` is a float, it will be converted to an integer before addition.
       The result of the addition is returned.
       
       Args:
            a (int or float): The first number.
            b (int or float): The second number. Defaults to 98.
       
       Returns:
            int: The sum of `a` and `b`.

        Raises:
            TypeError: If either `a` or `b` is not an integer or a float.
            Examples:
                >>> add_integer(3, 5)
                8
                >>> add_integer(3.5, 2)
                5
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            return int(a) + b
        elif type(b) is float:
            return a + int(b)
        return a + b
