#!/usr/bin/python3
"""To Define a text file-reading function."""


def read_file(filename=""):
    """reads the file
    """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
