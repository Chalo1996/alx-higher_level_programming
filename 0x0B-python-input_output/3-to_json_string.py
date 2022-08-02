#!/usr/bin/python3
"""Contains the to_json_string function
"""

import json


def to_json_string(my_obj):
    """
    Returns a serialized object string

    Args:
        my_obj(str): Object to serialize
    Return:
        The return: serialized my_obj
    """
    return (json.dumps(my_obj))
