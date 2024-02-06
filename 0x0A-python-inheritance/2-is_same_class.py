#!/usr/bin/python3
"""Defines a function that checks the class"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class

    Args:
        obj (any): Object to check
        a_class (type): Class to match the type of obj to
    Returns:
        True if the object is exactly an instance of the specified class.
        Otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
