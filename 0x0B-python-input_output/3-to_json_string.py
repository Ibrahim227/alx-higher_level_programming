#!/usr/bin/python3
import json


def to_json_string(my_obj):
        """Write a string to a UTF8 text file.

    Args:
        my_obj (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    return json.dumps(my_obj)
