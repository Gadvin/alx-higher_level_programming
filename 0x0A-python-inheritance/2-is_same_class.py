#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """function that checks if two objects are EXACTLY the same class
    """

    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")
    return (type(obj) is a_class)
