#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt inverted operators, == and !="""

    def __eq__(self, value):
        """Overrides the == operator with the !="""

        return (self.real != value)

    def __ne__(self, value):
        """Overrides the != operator with the =="""

        return (self.real == value)
