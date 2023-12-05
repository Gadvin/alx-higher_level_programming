#!/usr/bin/python3
"""Defines a JSON-to-object function."""


def append_write(filename="", text=""):
    """function that appends onto a utf-8 encoded text file
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
