#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """appends a string at the end of a txt file"""
    with open(filename, 'a') as f:
        return f.write(text)
