#!/usr/bin/python3
"""Contains the from_json_string function
"""

import json


def from_json_string(my_str):
    """
    loads a serialized data

    Args:
        my_str(str): data to load

    Returns:
        The return: the json rep of my_str
    """
    return (json.loads(my_str))
