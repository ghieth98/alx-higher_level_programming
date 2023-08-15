#!/usr/bin/python3
"""Module for unittests for Base class"""

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def test_init_with_no_id(self):
        """Test init with no id"""
        b1 = Base()
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        self.assertEqual(b1.id, 3)

        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b2.id, b3.id - 1)

        b4 = Base()
        b5 = Base()
        b6 = Base()
        self.assertEqual(b4.id, b6.id - 2)

    def test_init_with_id(self):
        """Test init with id"""
        b1 = Base(9)
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        self.assertEqual(b1.id, 9)

        b2 = Base(15)
        assert isinstance(b2, Base)
        assert hasattr(b2, 'id')
        self.assertEqual(b2.id, 15)

    def test_create_rectangle(self):
        """Test creating a rectangle"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle_dict = rectangle.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle_dict)
        self.assertEqual(str(rectangle), str(rectangle2))

    def test_create_square(self):
        """Test creating a square"""
        s = Square(1, 2, 3, 4)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertEqual(str(s), str(s2))

    def test_empty_to_json_string(self):
        """Test passing empty list to the method"""
        empty_list = []
        empty_json = Base.to_json_string(empty_list)
        self.assertEqual(empty_json, "[]")

    def test_rectangle_to_json_string(self):
        """Test passing rectangle to json"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        Rectangle.save_to_file([r1, r2])
        output_list = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output_list[0]))

    def test_square_to_json_string(self):
        """Test passing square to json"""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        output_list = Square.load_from_file()
        self.assertEqual(str(s1), str(output_list[0]))

    def test_empty_from_json_string(self):
        """Test converting empty string to list"""
        empty_list = Base.from_json_string("[]")
        self.assertEqual(empty_list, [])

    def test_rectangle_from_json_string(self):
        """Test converting rectangle string to list"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output_list = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output_list[0]))

    def test_square_form_json_string(self):
        """Test converting square string to list"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(10, 7, 2, 8)
        Square.save_to_file([s1, s2])
        output_list = Square.load_from_file()
        self.assertEqual(str(s1), str(output_list[0]))

    def test_rectangle_save_to_file(self):
        """Test save to file function with rectangle and square"""
        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"x": 3, "y": 4, "id": 5, "height": 2, "width": 1}, {"x": 3, "y": 2, "id": 1, "height": 4, "width": 5}]')

        s = Square(1, 2, 3, 4)
        s2 = Square(5, 4, 3, 2)
        Square.save_to_file([s, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 4, "x": 2, "size": 1, "y": 3}, {"id": 2, "x": 4, "size": 5, "y": 3}]')

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        """ tests loading from a file"""
        r = Rectangle(1, 2, 3, 4, 5)

        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r, r2])
        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 2)

        s = Square(1, 2, 3, 4)
        s2 = Square(5, 4, 3, 2)
        Square.save_to_file([s, s2])
        obj_list = Square.load_from_file()
        self.assertEqual(len(obj_list), 2)
