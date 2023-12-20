#!/usr/bin/python3
""" Square Module"""


class Square:
    """ Square Docstring"""
    def __init__(self, size=0):
        """ Constructor
        Args:
            size (int): area as int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Docstring for function"""

        return self.__size**2
