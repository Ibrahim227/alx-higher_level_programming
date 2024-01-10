#!/usr/bin/python3
"""Defines a fuynction"""


class BaseGeometry:
    """Defines class BaseGeometry"""
    def area(self):
        """Raise and Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(("{} must be an integer".format(name))
        if value <= 0:
            raisae ValueError("{} must be greater than 0".format(name))
