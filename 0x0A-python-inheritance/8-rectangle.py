#!/usr/bin/python3
"""Defines a fuynction"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines class Rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
