#!/usr/bin/python3
"""Defines a write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Returns:
        the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as myFile:
        return (myFile.write(text))
