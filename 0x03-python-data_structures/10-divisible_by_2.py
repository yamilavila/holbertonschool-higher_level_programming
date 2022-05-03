#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tmp = []
    for a in my_list:
        if a % 2 == 0:
            tmp.append(True)
        else:
            tmp.append(False)
    return tmp
