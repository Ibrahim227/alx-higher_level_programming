#!/usr/bin/python3
"""Defines a fuynction"""


class BaseGeometry:
    """Defines class BaseGeometry"""
    def __init__(self, width, height):
        """constructor"""
        self.__width = width
        self.__height = height

        if self.__width and self.__height < 0:
            break
