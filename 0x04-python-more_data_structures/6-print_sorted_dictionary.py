#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for a in sorted(a_dictionary.keys()):
        print("{}: {}".format(a, a_dictionary.get(a)))
