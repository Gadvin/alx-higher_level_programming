#!/usr/bin/python3
"""Function that Defines a file-writing function."""


def write_file(filename="", text=""):
    """function to get the number of lines from filename

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
