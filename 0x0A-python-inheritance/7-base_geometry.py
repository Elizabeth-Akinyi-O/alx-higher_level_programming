#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class body"""

    def area(self):
        """Raises an Exceptionerror message
            'area() is not implemented'
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
