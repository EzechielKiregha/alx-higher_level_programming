#!/usr/bin/python3
""" Square class definition """


class Square:
    """class representing the square"""
    def __init__(self, size=0):
        """initializing private attribute size of the square"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """area method definition, area of the square"""
        return self.__size * self.__size
