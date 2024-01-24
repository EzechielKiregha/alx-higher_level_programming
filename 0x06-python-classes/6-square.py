#!/usr/bin/python3
""""Coordinates of a square"""


class Square:
    """this class just represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the size private attribute"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """position method"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is int and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """"printing method of the square"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
