#!/usr/bin/python3
"""Defines function"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
