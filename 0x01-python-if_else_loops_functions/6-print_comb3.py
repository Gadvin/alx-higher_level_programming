#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0:
            first_digit = 0
        else:
            first_digit = i
        if i * 10 + j < 89:
            print(f"{first_digit}{j}".format(i, j), end=', ')
        else:
            print("{:d}".format(89))
