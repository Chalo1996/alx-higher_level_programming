#!/usr/bin/python3
"""Contains the Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Creates private instance attributes
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """defines a width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Defines a width setter
        """
        self.__width = width

    @property
    def height(self):
        """defines a height getter
        """
        return self.__height

    @height.setter
    def width(self, height):
        """Defines a height setter
        """
        self.__height = height

    @property
    def x(self):
        """defines a x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Defines a x setter
        """
        self.__x = x

    @property
    def y(self):
        """defines a y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Defines a y setter
        """
        self.__y = y
