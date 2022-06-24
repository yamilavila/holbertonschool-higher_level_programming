#!/usr/bin/python3
"""Task 3:
    Area of a square"""


class Square:
    """
    Class that defines a square that returns the
    current square area"""
    def __init__(self, size=0):
        self.__size = size
    """This methot initialize the class"""

    def area(self):
        """THis other method is for calculation of the area square"""
        self.area = self.__size * self.__size
        return self.area
