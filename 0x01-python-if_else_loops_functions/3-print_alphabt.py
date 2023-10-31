#!/usr/bin/python3
for character in range(97, 123):
    if (character == 101) | (character == 113):
        continue
    print(chr(character).format(), end="")
