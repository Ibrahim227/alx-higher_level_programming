#!/usr/bin/python3
""" Square Module"""


class Square:
    """
    Class Docstring
    """
    def __init__(self, size=0):
        """ Constructor
            Args:
                size(int): new value
        """
        self.size = size

    @property
    def size(self):
        """ get current squaure size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ return value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Function Docstring"""
        return (self.__size * self.__size)
