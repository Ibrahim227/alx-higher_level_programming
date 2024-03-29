#!/usr/bin/python3
"""Documentation of module import"""
from models.base import Base


class Rectangle(Base):
    """Defines class Rectangle that inherit from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Defines the constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """method so that it returns [Rectangle]"""
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
            }

    def to_csv(self):
        """Defines a ffunction to convert to csv"""
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def from_csv(cls, row):
        """Defines function from csv"""
        return cls(*map(int, row))
