#!/usr/bin/python3
"""
Define a Rectangle class
"""


class Rectangle:
    """Define the Rectangle class by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the Rectangle instance."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle instance.
        Args:
            value: value of the width, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the Rectangle instance."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance.
        Args:
            value: value of the height, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable representation of the
            Rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for a in range(self.__height):
            [rect.append('#') for b in range(self.__width)]
            if a != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

