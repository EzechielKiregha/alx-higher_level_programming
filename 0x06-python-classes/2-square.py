#!/usr/bin/python3
""" Defining a class """


class Square:
    """ represent a square in short """
    def __init__(self, size=0):
        """ initializing the size of the square """
        try:
            if size < 0:
                raise ValueError
            elif type(size) is not int:
                raise TypeError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
