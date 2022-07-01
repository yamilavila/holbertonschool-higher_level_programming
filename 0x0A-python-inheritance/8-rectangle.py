#!/usr/bin/python3
"""
Task 8: Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializer
        """
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
