#!/usr/bin/python3
""" Privacy is important in most cases """


class Square:
    """ Square class representing a square
    Attributes:
        __size is private instance attrubute
    """
    def __init__(self, n=0):
        """ The Constractor of a class
        Args:
            n is an integer and size of the square
        """
        self.__size = n
