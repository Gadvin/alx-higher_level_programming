#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """funtion to check if an object is sort of a class
    """

    if not isinstance(a_class, type):
        raise TypeError("a_class type must be 'type'")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
