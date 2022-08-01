#!/usr/bin/python3
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

    return obj.__dict__
