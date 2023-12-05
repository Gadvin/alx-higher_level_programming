#!/usr/bin/python3
""" Has the MyList class"""


class MyList(list):
    """ifunction to extended version of list
    """
    def print_sorted(self):
        """function to prints the list in ascending order
        """
        copy = self[:]
        copy.sort()
        print(copy)
