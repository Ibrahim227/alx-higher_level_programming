#!/usr/bin/python3
"""Defines a fuynction"""


class BaseGeometry:
    """Defines class BaseGeometry"""
    def area(self):
        """Raise and Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        self.name = name
        self.value = value
        
    if value <= 0:
        raisae Exception("<name> must be greater than 0")
    if value != int:
        raise Exception("<name> must be an integer")
