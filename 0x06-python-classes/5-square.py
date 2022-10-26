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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Define area of a square.
        Returns:
            The return value. Square of size
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Define a method to print a square of "#" characters

        Print the "#" equivalent to the area of the square
        print empty line if size == 0

        """
        if self.size == 0:
            print()

        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
