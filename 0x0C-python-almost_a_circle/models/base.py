#!/usr/bin/python3

"""
Base Class model
"""
import json


class Base:
    """
       Base class for other classes and sets
        up a private class attribute
       for counting the number of objects
        and a constructor for initializing
       instance ID values.
       """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for initializing
         the instance id values.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Json string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the json string
        representation of list_objs to file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of Json string
         representation json_string
        """
        if json_string is None or json_string == '[]':
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with
         all attributes already set
        """

        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            return None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of
         instances from a Json file
         """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                content = f.read()
        except FileNotFoundError:
            return []

        content_list = cls.from_json_string(content)
        instance_list = [cls.create(**obj_dict) for obj_dict in content_list]
        return instance_list
