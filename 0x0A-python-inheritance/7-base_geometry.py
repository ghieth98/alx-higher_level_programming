#!/usr/bin/python3
"""
Empty class BaseGeometry
"""


class BaseGeometry:
    """class BaseGeometry"""

    def integer_validator(self, name, value):

        """ int validator """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):

        """ public instance method not implemented"""

        raise Exception("area() is not implemented")
