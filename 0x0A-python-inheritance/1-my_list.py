#!/usr/bin/python3
"""
Contains the MyList class
"""


class MyList(list):
    """
    Args:
        list: The super class
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        prints the sorted list
        """

        print(sorted(self))
