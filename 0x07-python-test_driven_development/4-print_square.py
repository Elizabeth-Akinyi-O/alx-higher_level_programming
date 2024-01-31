#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Prints a square using the character #
    Args:
        size (int): The height or width of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print("")
