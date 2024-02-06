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

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
