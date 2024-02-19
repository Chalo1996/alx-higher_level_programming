#!/usr/bin/python3
"""Creates a class object"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Creates field size of size parameter
        Args:
            size: The size of the square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Define a getter for the position attribute

        Return:
            The return value. The private attribute __postion
        """
        return self.__position

    @position.setter
    def position(self, tuples):
        """
        Define a setter for the position attribute

        Args:
            tuples (int): tuples to be passed to the private \
                            attribute position

        Return:
            The return tuples. None.
        """
        if not isinstance(tuples, tuple) or \
           len(tuples) != 2 or not isinstance(tuples[0], int) or \
           not isinstance(tuples[1], int) or \
                tuples[0] < 0 or tuples[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = tuples

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

    def my_print(self):
        """
        Define a method to print a square of "#" characters
        Print the "#" equivalent to the area of the square
        print empty line if size == 0

        Return:
            The return. None.
        """

        if self.__size == 0:
            print("")

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
