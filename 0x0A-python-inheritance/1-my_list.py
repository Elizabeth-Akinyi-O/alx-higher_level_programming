#!/usr/bin/python3
"""Defines MyList that inherits from list"""


class MyList(list):
    """Implements the print_sorted().
        Method:
        print_sorted - prints the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        return (sorted(self))
