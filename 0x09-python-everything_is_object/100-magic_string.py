#!/usr/bin/python3
def magic_string(occurrence=[0]):
    occurrence[0] = occurrence[0] + 1
    return ("BestSchool" + (", BestSchool" * (occurrence[0] - 1)))
