#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """Represents a Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            # k is key
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)
