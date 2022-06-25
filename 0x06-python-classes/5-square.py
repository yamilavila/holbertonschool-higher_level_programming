#!/usr/bin/python3
"""
Task 5: Printing a square
"""


class Square:
    """
    Square class
    Atributte:
    size
    """
    def __init__(self, size=0):
        """Init method,
        initialize the class
        """
        self.size = size

    def area(self):
        """ Returns the current
        square area
        """
        return (self.__size**2)

    @property
    def size(self):
        """Retrieve the current
        size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter method
        to set it
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square
        with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print("")
