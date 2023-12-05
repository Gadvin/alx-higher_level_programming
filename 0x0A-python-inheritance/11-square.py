#!/usr/bin/python3
"""Class base"""

Rectangle = __import__('9-rectangle').Rectangle

"""Square class"""


class Square(Rectangle):
    """A square shape class,
    super class is BaseGeometry,
    then Rectangle
    """

    def __init__(self, size):
        """function to instantiation method for class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """function to overide magic str method for class
        """
        string = "[Square] " + str(self.__size) + '/'
        string += str(self.__size)
        return string
