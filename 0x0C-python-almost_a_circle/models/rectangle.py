#!/usr/bin/python3

"""
class Rectangle Model
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for initialization
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets the current width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the current height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Gets the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Gets the value for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for i in range(self.__y):
            print()

        for n in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Return the string representation of the class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Assign argument to each attribute
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a rectangle
        """
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
