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
        if (isinstance(value, tuple) or len(value) == 2 or
                all(isinstance(item, int) for item in value) or
                all(item >= 0) for item in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """"printing method of the square"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
