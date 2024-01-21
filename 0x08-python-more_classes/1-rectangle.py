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
        if value < 0:
            raise TypeError("width must be >= 0")
        elif value
