#!/usr/bin/python3
"""Contins the inherits_from module
"""


def inherits_from(obj, a_class):
    """Returns issubclass object a_class
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
