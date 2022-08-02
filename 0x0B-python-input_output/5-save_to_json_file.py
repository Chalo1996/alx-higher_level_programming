#!/usr/bin/python3
"""Contains the save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Returns a serialized object to a file

    Args:
        my_obj(str): Object to serialize
        filename(file; txt): file to dump to

    Return:
        The return: serialized my_obj
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
