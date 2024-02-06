#!/usr/bin/python3
"""Defines a (directly or indirectly) inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if the object is exactly an inherited
        instance of the specified class

    Args:
        obj (any): Object to check
        a_class (type): Class to match the type of obj to
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        Otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
