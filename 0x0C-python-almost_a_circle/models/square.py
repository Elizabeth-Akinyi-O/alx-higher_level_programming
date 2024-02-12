#!/usr/bin/python3
"""Defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square

        Args:
            size (int): Size of the new Square
            x (int): x coordinate of the new Square
            y (int): y coordinate of the new Square
            id (int): Identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/Get the size of the new Square"""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square

        Args:
            *args (ints): New attribute values
            - 1st argument - id
            - 2nd argument - size
            - 3rd argument - x
            - 4th argument - y
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Returns the dictionary representation of the new Square"""
        return ({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        })

    def __str__(self):
        """Returns the print() && str() representation of the new Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
