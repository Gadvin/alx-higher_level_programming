#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if(idx < 0) or (idx > length - 1):
        return("None")
    return(my_list[idx])
