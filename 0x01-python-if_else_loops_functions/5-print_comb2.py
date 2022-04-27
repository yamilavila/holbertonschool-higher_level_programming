#!/usr/bin/python3
for numbrs in range(0, 100):
    if numbrs < 99:
        print("{:02d}, ".format(numbrs), end='')
    else:
        print("{:02d}".format(numbrs))
