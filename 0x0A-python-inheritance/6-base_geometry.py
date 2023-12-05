#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry():
    """function for use with shapes. Super class.
    """

    def area(self):
        """function instance method to calculate area of shape
        """
        raise Exception("area() is not implemented")
