#!/usr/bin/python3
"""Contains the MyInt class
"""


class MyInt(int):
    """Inverts the == and != operators for int
    """

    def __new__(cls, *args, **kwargs):
        """implement new instance of the class
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, x):
        """Invert != for ==
        """
        return int(self) != x

    def __ne__(self, x):
        """Invert == for !=
        """
        return int(self) == x
