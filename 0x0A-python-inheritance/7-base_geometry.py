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
    try:    
        if self.value <= 0:
            print("")
    except TypeError:
        print("<name> must be greater than 0")
