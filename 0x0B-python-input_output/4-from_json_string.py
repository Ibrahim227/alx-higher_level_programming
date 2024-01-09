#!/usr/bin/python3
"""Defines a str json to obj"""
import json


def from_json_string(my_str):
    """Returns an obj"""
    return json.loads(my_str)
