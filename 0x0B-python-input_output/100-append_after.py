#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after
        each line containing a specific string

    Args:
        filename (str): Name of the file
        search_string (str): String to search
        new_string (str): String to insert
    """

    text = ""
    with open(filename) as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as writing:
        writing.write(text)
