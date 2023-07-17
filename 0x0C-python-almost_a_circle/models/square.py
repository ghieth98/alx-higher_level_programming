#!/usr/bin/python3
"""
class Square model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class for square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        Gets the value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the value of size
        """
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        Assign an argument to each attribute
        """
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of a square"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
