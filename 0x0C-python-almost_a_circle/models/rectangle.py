#!/usr/bin/python3
"""Documentation of module import"""


class Rectangle(Base):
    """Defines class Rectangle that inherit from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Defines the constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    super().__init__(self, id=None)
