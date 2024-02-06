#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object

    Args:
        obj (any): The object to add an attribute
        att (str): Name of the attribute to add to object
        value (any): Value of attribute (att)
    Raises:
        TypeError: can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
