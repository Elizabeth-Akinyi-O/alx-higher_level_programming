#!/usr/bin/python3

"""Define a magic class matching a bytecode by Alx."""
import math


class MagicClass:
    """Initialize a MagicClass."""

    def __init__(self, radius=0):
        """Construct the MagicClass.

        Args:
            radius (float || int): The radius of the new MagicClass.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate and return the araea of the MagicClass."""
        return (self._MagicClass__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate the circumference of the MagicClass."""
        return (self._MagicClass__radius * 2 * math.pi)
