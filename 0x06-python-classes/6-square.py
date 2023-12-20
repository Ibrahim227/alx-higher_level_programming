#!/usr/bin/python3
""" Square Module"""


class Square:
    """Square class Docstring"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor
            Args:
                size (int)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get/set the current size size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ retrieve value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ docstring function for position"""
        return (self.__size)

    @position.setter
    def position(self, value):
        """Docstring for position function"""
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculate the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ print # square"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
