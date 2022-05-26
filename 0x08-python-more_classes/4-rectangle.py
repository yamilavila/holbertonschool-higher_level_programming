#!usr/bin/python3
"""Task 4:
Eval is magic
"""


class Rectangle:
    """Define a rectangle"""
    def __init__(self, width=0, height=0):
        """init attribute"""
        self.width = width
        self.height = height

    def __str__(self):
        if self.area() == 0:
            return ""
        return (('#' * self.__width + '\n') * self.__height)[:-1]

    def __repr__(self):
        return 'Rectangle({:d}, {:d}'.format(self.__width, self.__height)

    @property
    def width(self):
        """property method"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if type(value) is not int:                                                            
            raise TypeError("width must be an integer")                                       
        if value < 0:                                                                         
            raise ValueError("width must be >= 0")                                            
        self.__width = value                                                                  
                                                                                              
    @property                                                                                 
    def height(self):                                                                         
        """prperty method"""                                                                  
        return self.__height                                                                  
                                                                                              
    @height.setter                                                                            
    def height(self, value):                                                                  
        """sets the height of the value"""                                                    
        if type(value) is not int:                                                            
            raise TypeError("height must be an integer")                                      
        if value < 0:                                                                         
            raise ValueError("height must be >= 0")                                           
        self.__height = value                                                                 
                                                                                              
    def area(self):                                                                           
        """calculation of the area"""                                                         
        return self.__height * self.__width                                                   
                                                                                              
    def perimeter(self):                                                                      
        """calculation of the perimeter"""                                                    
        if self.width == 0 or self.height == 0:                                               
            return 0                                                                          
        return 2 * (self.__height + self.__width)
