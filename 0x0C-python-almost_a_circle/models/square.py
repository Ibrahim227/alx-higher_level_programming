#!/usr/bin/python3
"""Documentation Modules"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines class Square that inherit from class Rectanglee"""
    def __init__(self, size, x=0, y=0, id=None):
        """Defines the constructor"""
        super().__init__(size, size, x, y, id=None)

    @propety
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Override str methode for Square"""
        return (
                f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}
        )
