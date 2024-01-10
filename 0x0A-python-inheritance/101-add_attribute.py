#!/usr/bin/python3
"""Defines a function"""


def add_attribute(obj, attr, value):
    """Adds attribute to an obj if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
