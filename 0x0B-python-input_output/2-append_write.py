#!/usr/bin/python3
"""Function that Defines a file-appending function."""


def read_lines(filename="", nb_lines=0):
    """function to read no of  lines from file and prints to stdout
    """
    printed = 0
    with open(filename, encoding='utf-8') as myFile:
        for line in myFile:
            if printed < nb_lines or nb_lines <= 0:
                print(line, end='')
                printed += 1
