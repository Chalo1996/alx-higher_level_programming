#!/usr/bin/python3
"""
The lookup function.Computes for the atributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available attributes\
    and methods of an object

    Args:
        obj: The object

    Return:
        The return. atributes and methods of the\
        object
    """

    return dir(obj)
