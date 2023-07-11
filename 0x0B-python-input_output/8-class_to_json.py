#!/usr/bin/python3
"""
Module class to json
"""


def class_to_json(obj):
    """returns directory description with simple data structure"""
    return obj.__dict__
