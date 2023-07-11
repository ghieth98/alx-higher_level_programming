#!/usr/bin/python3
"""
Module class Student
"""


class Student:
    """Defines student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the student"""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """Replace all attributes of the student"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
