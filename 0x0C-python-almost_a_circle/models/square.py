#!/usr/bin/python3
"""Documentation Modules"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines class Square that inherit from class Rectanglee"""
    super().__init__(id, x, y, width, height)
    def __init__(self, size, x=0, y=0, id=None):
        """Defines the constructor"""
        self.size = size
        self.x = x
        self.y = y
    self.width = size
    self.height = size
    return size
