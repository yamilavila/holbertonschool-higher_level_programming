#!/usr/bin/python3
"""
0.Read file
"""


def read_file(filename=""):
    """ Function that reads a text file (UTF8) and prints it to stdout"""
    with open("my_file_0.txt", mode="r", endcoding='utf8') as f:
        print(f.read(), end="")
