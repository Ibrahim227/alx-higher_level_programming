#!/usr/bin/python3
"""Doctstring"""


class Rectangle:
    """Defines a class Rectangle"""
    def __init__(self, width, height):
        """Defines the constructor"""
        self.__width = width
        slef.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
