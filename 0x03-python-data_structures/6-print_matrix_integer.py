#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in range(len(matrix)):
        for element in range(len(matrix[rows])):
            print("{:d}".format(matrix[rows][element]), end="")
            if element != (len(matrix[rows]) - 1):
                print(" ", end="")
        print()
