#!/usr/bin/python3
"""Defines a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints a name
    Args:
        first_name (str): 1st name to be printed
        last_name (str): last name to be printed
    Raises:
        TypeError: first_name must be a string or
        last_name must be a string if !str
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
