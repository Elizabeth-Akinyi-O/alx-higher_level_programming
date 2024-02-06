#!/usr/bin/python3
"""Defines an append_write module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): Name of the file to append to
        text (str): String to append
    Returns:
        The number of characters added
    """

    with open(filename, "a", encoding="utf-8") as myFile:
        return (myFile.write(text))
