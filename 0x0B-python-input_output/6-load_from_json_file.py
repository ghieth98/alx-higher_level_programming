#!/usr/bin/python3
"""Module load to json file"""
import json


def load_to_json_file(filename):
    """
    function that creates an Object from a JSON file
    """

    with open(filename) as f:
        return json.loads(f.read())
