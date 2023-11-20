#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    i = 0
    try:
        for i in range(x):
            number = my_list[i]
            if isinstance(number, int):
                print("{:d}" .format(number), end="")
                length += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
    return length
