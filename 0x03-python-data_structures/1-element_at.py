#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    if idx < 0 or idx >= a:
        return  None
    return my_list[idx]
