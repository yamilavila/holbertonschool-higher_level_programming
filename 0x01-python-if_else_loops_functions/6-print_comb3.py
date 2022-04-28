#!/usr/bin/python3
for numbr1 in range(0, 9):
    for numbr2 in range(0, 10):
        if numbr1 < numbr2 and numbr1 != 8:
            print("{:d}{:d}, ".format(numbr1, numbr2), end='')
        if numbr1 < numbr2 and numbr1 == 8:
            print("{:d}{:d},".format(numbr1, numbr2))
