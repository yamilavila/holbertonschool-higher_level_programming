#!/usr/bin/python3
"""
Task 6:
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize
        """
        self.size = size
        self.position = position

    def area(self):
        """Returns current square
        area
        """
        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square with
        the character #
        """

    if self.__size == 0:
        print("")
    else:
        for x1 in range(0, self.__position[1]):
            print("")
        for y1 in range(0, self.__size):
            for x2 in range(0, self.__position[0]):
                print(" ", end="")
            for y2 in range(0, self.__size):
                print("#", end="")
            print("")

    @property
    def size(self):
        """getter method to retrieve
        size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method to set the size
        of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """setter method for position must be
        a tuple of 2 int
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position must be
        a tuple of 2 int
        """
        flag = False
        if type(value) is tuple:
            if len(value) == 2:
                if type(value[0]) is int and value[0] >= 0:
                    if type(value[1]) is int and value[1] >= 0:
                        flag = True
                        self.__position = value
        if flag is False:
            raise TypeError("position must be a tuple of 2 positive integers")
