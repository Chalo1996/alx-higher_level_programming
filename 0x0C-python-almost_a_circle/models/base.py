#!/usr/bin/python3
"""Contains the Base class
"""


class Base:
    """Base class for other classes

    Creates a private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
