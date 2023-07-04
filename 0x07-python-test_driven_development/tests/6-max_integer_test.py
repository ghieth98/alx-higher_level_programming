#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_positive_case(self):
        """ test positive values """
        self.assertEquals(max_integer([1, 2, 3, 4]), 4)

    def test_negative_case(self):
        """ test negative values """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_unsorted(self):
        """ test unsorted values """
        self.assertEqual(max_integer([5, 2, 6, 7, 9]), 9)

    def test_one_element(self):
        """ test one element in list """
        self.assertEqual(max_integer([5]), 5)

    def test_mixed_numbers(self):
        """ tests mixed numbers values"""
        self.assertEqual(max_integer([-2, -9, 1, 0]), 1)

    def test_floats(self):
        """ tests floats values"""
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

    def test_string(self):
        """ tests raising error in case of a string"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])
