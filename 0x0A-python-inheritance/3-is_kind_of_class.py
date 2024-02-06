#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is exactly an instance, or an inherited
        instance of the specified class

    Args:
        obj (any): Object to check
        a_class (type): Class to match the type of obj to
    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class.
        Otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
