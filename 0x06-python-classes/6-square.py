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
        self.__sizetypechecker(size)
        self.__positionchecker(position)
        self.__size = size
        self.__position = position

    def __sizetypechecker(self, size):
        """
        Checks if size is an integer
        Args:
            size: The size to be checked
        Return:
            The return size. True if size is an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return True

    def __positionchecker(self, position):
        """
        Checks if position is a tuple of 2 positive integers
        Args:
            size: The position to be checked
        Return:
            The return position. True if position is a tuple of 2 positive \
                            integers
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(
                position[0],
                int) or not isinstance(
                position[1],
                int):
            raise TypeError("position must be a tuple of 2 positive integers")
        for pos in position:
            if pos < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        return True

    @property
    def position(self):
        """
        Define a getter for the position attribute

        Return:
            The return position. The private attribute __postion
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
        self.__positionchecker(tuples)
        self.__position = tuples

    @property
    def size(self):
        """
        Defines a getter method for the size attribute
        Return:
            The return size. private size attribute
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Creates a setter for the private attribute size
        Args:
            size: The parameter to assign to the attribute
        Instructions:
            Raise TypeError if size is not an integer and
            sizeError if size is negative
        """
        self.__sizetypechecker(size)
        self.__size = size

    def area(self):
        """
        Define area of a square.
        Returns:
            The return size. Square of size
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

        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()  # Adjust for vertical position

            for _ in range(self.size):
                # Check if line should be filled with spaces based on
                # position[1]
                if self.__position[1] > 0:
                    continue  # Print without spaces
                # Add spaces for horizontal positioning
                for _ in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.size)
