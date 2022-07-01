#!/usr/bin/python3
"""
Task 10: Square #1
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializer
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
