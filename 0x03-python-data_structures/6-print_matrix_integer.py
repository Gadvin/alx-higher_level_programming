#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for element in rows:
            print("{:d}".format(element), end=" ")
        print()
