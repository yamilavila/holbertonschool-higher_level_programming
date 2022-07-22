#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """writes to a file overwritin it"""
    with open(filename, 'w') as f:
        return f.write(text)
