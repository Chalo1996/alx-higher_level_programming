#!/usr/bin/python3
"""Contains the write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to file
    """
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return f.tell()
