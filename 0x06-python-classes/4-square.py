#!/usr/bin/python3
"""

Task 4. Access and update private attribute
"""

class Square:
    """
    Square class
    Atributte:
    Private instance attribute: size:
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Property that gets the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        if type(value) is int:
        """ 
        if type(value) is int:
            self.__size = value
        else: 
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """
        Methodto calculate the area of square
        """
        return self.__size ** 2
