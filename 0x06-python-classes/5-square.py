#!/usr/bin/python3
"""Square class definition"""


class Square:
    """this class just represent a square"""

    def __init__(self, size=0):
        """initialize the size private attribute"""
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculating the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """"printing method of the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
