#!/usr/bin/python3
"""in this module the my_list class inherit the List class"""


class MyList(list):
    """It's subclass of the list class"""

    def __init__(self):
        """We initialize the object attributes"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list out"""
        print(sorted(self))
