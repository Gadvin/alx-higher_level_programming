#!/usr/bin/python3
"""module for use in testing
    rectangle class
"""


import sys
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """class for test case for rectangle class
    """

    def test_basic_id(self):
        """
        used to test the basic functionality
        """
        b = Square(10, 2)
        b2 = Square(2, 10)
        b3 = Square(3, 10)
        self.assertEqual(b2.id + 1, b3.id)

    def test_given_id(self):
        """
        used to test the given id, not generated by init
        """
        b = Square(10, 2)
        b2 = Square(10, 3)
        b3 = Square(10, 4)
        b4 = Square(10, 5, 0, 42)
        self.assertEqual(b2.id + 1, b3.id)
        self.assertEqual(42, b4.id)

    def test_input_types(self):
        """
        used to test the type errors when creating a square
        """
        with self.assertRaises(TypeError):
            n = Square("hello", "world")
        with self.assertRaises(TypeError):
            n = Square(5.4, 3.8)
        with self.assertRaises(TypeError):
            n = Square(4, 8, "hello", "world")
        with self.assertRaises(TypeError):
            n = Square(4, 8, 5.12, 5.9)
        with self.assertRaises(TypeError):
            n = Square(True, False, True, 49)

    def test_input_values(self):
        """
        used to test the value errors when creating a square
        """
        with self.assertRaises(ValueError):
            n = Square(0, 0)
        with self.assertRaises(ValueError):
            n = Square(1, 1, -5, -2)

    def test_area(self):
        """
        used to test that the area method for squares works
        """
        r = Square(4, 8)
        self.assertEqual(r.area(), 16)

    def test_str(self):
        """
        used to test the custom str method for our square object
        """
        r = Square(3, 3, 2, 14)
        self.assertEqual("[Square] (14) 3/2 - 3", str(r))
        r = Square(5, 5, 1)
        self.assertEqual("[Square] ({}) 5/1 - 5".format(r.id), str(r))

    def test_update(self):
        """
        used to test the update method of a square using args
        """
        r = Square(4, 5, 45)
        r.update(500)
        self.assertEqual(500, r.id)
        r.update(500, 2)
        self.assertEqual(2, r.size)
        r.update(500, 2, 3)
        self.assertEqual(3, r.x)
        r.update(500, 2, 3, 4)
        self.assertEqual(4, r.y)
        r.update(500, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(4, r.y)

    def test_kwarg_update(self):
        """
        used to test the update method of the square using kwargs
        """
        r = Square(5, 0, 0, 33)
        r.update(45, id=32, size=42)
        self.assertEqual(45, r.id)
        r.update(45, 10, x=5, y=6)
        self.assertEqual(0, r.x)
        self.assertEqual(10, r.size)
        self.assertEqual(45, r.id)
        r.update(size=4)
        self.assertEqual(4, r.size)
        r.update(size=6, id=6)
        self.assertEqual(6, r.size)
        self.assertEqual(6, r.id)
        r.update(x=100, y=100)
        self.assertEqual(6, r.id)
        self.assertEqual(100, r.x)
        self.assertEqual(100, r.y)

    def test_size(self):
        """
        used to test the basic size changes for square
        """
        r = Square(5, 0, 0, 45)
        r.size = 82
        self.assertEqual(82, r.height)
        self.assertEqual(82, r.size)
        self.assertEqual(82, r.width)

    def test_size_values(self):
        """
        used to test the size changes raises value errors properly
        """
        r = Square(5, 0, 0, 45)
        with self.assertRaises(ValueError):
            r.size = 0
        with self.assertRaises(ValueError):
            r.size = -42

    def test_size_types(self):
        """
        used to test the size changes raise type errors properly
        """
        r = Square(5, 0, 0, 45)
        with self.assertRaises(TypeError):
            r.size = 4.0
        with self.assertRaises(TypeError):
            r.size = "holberton"
        with self.assertRaises(TypeError):
            r.size = True

    def test_to_dictionary(self):
        """
        used to test the square's to_dictionary method
        """
        r = Square(5, 1, 2, 33)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict['id'], 33)
        self.assertEqual(r_dict['size'], 5)
        self.assertEqual(r_dict['x'], 1)
        self.assertEqual(r_dict['y'], 2)
