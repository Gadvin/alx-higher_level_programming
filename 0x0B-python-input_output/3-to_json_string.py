#!/usr/bin/python3
"""Defines a string-to-JSON function."""


def write_file(filename="", text=""):
    """Function that writes to a utf-8 encoded text file
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(text)
