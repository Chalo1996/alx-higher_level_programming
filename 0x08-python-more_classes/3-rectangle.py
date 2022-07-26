#!/usr/bin/python3
"""
Describe a rectangle.
"""


class Rectangle:
    """
    Define a rectangle object class
    """

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): Default width for the class object.
            height (int): Default height for the class object.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Setter for the private attribute width
        Args:
            None
        Return:
            The return. The private attribute width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private attribute width
        Args:
            Value (int): value to set
        Return:
            The return. None
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter for the private attribute height
        Args:
            None
        Return:
            The return. The private attribute height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private attribute height
        Args:
            Value (int): value to set
        Return:
            The return. None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Return:
            The return. The area of the rectangle object
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Return:
            The return. The perimeter of the rectangle object
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Define a string representation of the rectangle class object
        """
        mystr = ""
        if self.__width != 0 and self.__height != 0:
            mystr += "\n".join("#" * self.__width
                               for i in range(self.__height))
        return mystr
