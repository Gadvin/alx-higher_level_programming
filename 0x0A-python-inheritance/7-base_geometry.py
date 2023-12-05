#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry():
    """function for use with shapes. Super class.
    """

    def area(self):
        """function instance method to calculate area of shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates integer input
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
