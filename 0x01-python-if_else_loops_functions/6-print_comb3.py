#!/usr/bin/python3

for numbr1 in range(10):
    for numbr2 in range(numbr1, 10):
        if numbr1 > numbr2:
            print("{:d}{:d}".format(numbr1, numbr2), end='')
            if numbr1 * 10 + numbr2 == 89:
                print('')
            else:
                print(', ', end='')
