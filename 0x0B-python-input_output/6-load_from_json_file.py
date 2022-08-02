#!/usr/bin/python3
"""Contains the load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file"

    Args:
        filename(file; txt): file to dump object

    Return:
     The return. None
    """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
