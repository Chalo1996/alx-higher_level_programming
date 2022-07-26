#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """

    prints a neatly formated name

    Args:
        first_name: user's first name
        last_name: optional last name

    Return:
        The return. None

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {:s} {:s}".format(first_name, last_name))

    else:
        print("My name is {:s}".format(first_name))
