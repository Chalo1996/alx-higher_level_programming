#!/usr/bin/python3
"""Contains the read_file function
"""


def read_file(filename=""):
    """Reads a text file
    """
    with open(filename, encoding="utf-8") as f:
        readfile = f.read()
        print(readfile)
