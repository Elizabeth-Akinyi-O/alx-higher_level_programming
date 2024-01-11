#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newDict = {key: value}
    a_dictionary.update(newDict)
    return a_dictionary
