#!/usr/bin/python3
"""Documentation Modules"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square that inherit from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Defines the constructor"""
        super().__init__(size, size, x, y, id=None)
        self.size = size

    def __str__(self):
        """overrides str method for Square"""
        return (
                f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}"
            )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        attr = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y
            }

    def to_csv(self):
        """Defines a ffunction to convert to csv"""
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def from_csv(cls, row):
        """Defines function from csv"""
        return cls(*map(int, row))
