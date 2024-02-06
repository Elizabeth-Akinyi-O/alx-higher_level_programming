#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry rectangle class body"""

    def __init__(self, width, height):
        """Initializes a new rectangle

        Args:
            height (int): Height of the new rectangle
            width 9int): width of the new rectangle
        """

        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """Returns the print() and str() representation of a rectangle"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
