#!/usr/bin/python3
"""
Task 9: Full rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializer with the args:
        width and height must be private.
        width and height must be positive int validated by integer_validator
        """
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        """
        Method:
        int: area > 0
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Build in funct for:
        string representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
