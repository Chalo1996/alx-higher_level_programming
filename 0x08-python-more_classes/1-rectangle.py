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
