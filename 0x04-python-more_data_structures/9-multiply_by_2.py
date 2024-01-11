#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for a in a_dictionary:
        newDict[a] = a_dictionary[a] * 2
    return newDict
