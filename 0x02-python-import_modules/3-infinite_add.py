#!/usr/bin/python3
import sys


def add_arguments(*args):
    result = 0
    for arg in args:
        result += int(arg)
    return result


if __name__ == '__main__':
    arguments = sys.argv[1:]

    # Check if there are arguments to add
    if arguments:
        # Call the add_arguments function and print the result
        result = add_arguments(*arguments)
        print(result)
    else:
        print("0")
