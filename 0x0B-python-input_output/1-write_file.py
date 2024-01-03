#!/usr/bin/python3
"""Function that Defines a file-writing function."""


def write_file(filename=""):
    """function to get the number of lines from filename

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, encoding='utf-8') as myFile:
        return sum([1 for line in myFile])
