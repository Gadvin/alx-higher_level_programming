#!/usr/bin/python3
"""To define  an object attribute lookup function."""


def lookup(obj):
    """function returns all objects of objects dictionary as a list
    """
    return dir(obj)
