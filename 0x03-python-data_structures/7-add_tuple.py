#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if length_a == 0:
        tuple_a1 = 0
        tuple_a2 = 0
    elif length_a == 1:
        tuple_a1 = tuple_a[0]
        tuple_a2 = 0
    else:
        tuple_a1 = tuple_a[0]
        tuple_a2 = tuple_a[1]

    if length_b == 0:
        tuple_b1 = 0
        tuple_b2 = 0
    elif length_b == 1:
        tuple_b1 = tuple_b[0]
        tuple_b2 = 0
    else:
        tuple_b1 = tuple_b[0]
        tuple_b2 = tuple_b[1]

    new_tuple = (tuple_a1 + tuple_b1, tuple_a2 + tuple_b2)

    return (new_tuple)
