#!/usr/bin/python3
"""Defines load_from_json_file module"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""

    with open(filename) as myFile:
        return json.load(myFile)
