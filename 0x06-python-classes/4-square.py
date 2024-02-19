#!/usr/bin/python3
"""Creates a class object"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """
        Creates field size of size parameter

        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Defines a getter method for the size attribute

        Return:
            The return value. private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Creates a setter for the private attribute size

        Args:
            value: The parameter to assign to the attribute

        Instructions:
            Raise TypeError if size is not an integer and
            ValueError if size is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Define area of a square.
        Returns:
            The return value. Square of size
        """
        return self.__size * self.__size
