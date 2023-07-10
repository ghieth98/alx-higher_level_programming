#!/usr/bin/python3
"""Module class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle and represents square
    """

    def __int__(self, size):
        """Initialize a new square"""
        self.integer_validator("size", size)
        super.__init__(size, size)
        self.__size = size
