#!/usr/bin/python3
"""Defines a text_indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after
        each of these characters: ., ? and :
    Args:
        text (str): Text to be printed
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # use i to iterate
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")

        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
