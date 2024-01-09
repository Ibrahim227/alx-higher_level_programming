#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an obj"""
    json.dumps("{}".format(my_obj))
