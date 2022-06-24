#!/usr/bin/python3
"""Task 2
Size validation"""


class Square:
    """Defines a square by:
        args size - size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """setting up the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
