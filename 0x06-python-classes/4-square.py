#!/usr/bin/python3
"""Square class definition"""

class Square:
    """this class represent a square
        methods:
            size (overloaded <setter & getter>)
    """
    def __init__(self, size=0):
        """initializing attribute size with a optional size of 0"""
        self.__size = size

    @property
    def size(self):
        """setting the getter of the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the getter of the value which is the square size"""
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
    
    def area(self):
        """defining the area method"""
        return self.__size ** 2
