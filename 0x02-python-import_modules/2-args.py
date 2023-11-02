#!/usr/bin/python3

import sys

Length = len(sys.argv)

if Length == 1:
    print("{} arguments.".format(Length - 1))

elif Length == 2:
    print("{} argument:".format(Length - 1))

else:
    print("{} arguments:".format(Length - 1))

for i in range(1, Length):
    print("{}: {}".format(i, sys.argv[i]))
