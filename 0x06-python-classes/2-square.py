#!/usr/bin/python3
""" Defining a class """


class Square:
    """ represent a square in short """
    def __init__(self, size=0):
        """ initializing the size of the square """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
