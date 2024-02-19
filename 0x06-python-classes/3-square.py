#!/usr/bin/python3
"""Creates an class object"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Creates a private instance attribute

        Args:
            size: The size of the square

        Instructions:
           size must be an integer othewise raise
           exception TypeError and must be >= 0
           otherwise raise exception ValueError.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Define area of a square.

        Returns:
            The return value. Square of size

        """
        return self.__size * self.__size
