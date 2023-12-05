#!/usr/bin/python3

class BaseGeometry():
    """function for use with shapes. Super class.
    """

    def area(self):
        """function instance method to calculate area of shape
        """
        raise Exception("area() is not implemented")
