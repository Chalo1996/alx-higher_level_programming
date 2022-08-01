#!/usr/bin/python3
"""The Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiates height and width
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Implements string format
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Implements the area
        """
        res = self.__height * self.__width
        return res
