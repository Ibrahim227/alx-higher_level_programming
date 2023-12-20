#!/usr/bin/python3
""" Square Module"""


class Square:
    """
    This is a class Docstring
    """
    def __init__(self, size=0):
        """ Constructor
        Args:
            size (int): the size of new str
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
