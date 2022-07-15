#!/usr/bin/python3
"""class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Private attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """obj init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
iiii 
    def area(self):
        """calcula el area y returns width * height"""
        return self.width * self.height

    def display(self):
        """prints stdout instance with character #"""
        print('\n' * self.y, end="")
        print((" " * self.x + ("#" * self.width) + '\n') * self.height, end="")

    def update(self, *args, **kwargs):
        """arg count"""
        cnt = len(args)
        if cnt > 0:
            self.id = args[0]
            if cnt > 1:
                self.width = args[1]
                if cnt > 2:
                    self.height = args[2]
                    if cnt > 3:
                        self.x = args[3]
                        if cnt > 4:
                            self.y = args[4]

        elif kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dict"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
