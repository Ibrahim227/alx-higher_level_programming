#!/usr/bin/python3
"""Defines function"""


def is_same_class(obj, a_class):
    """Returns true for isinstance, otherwise False"""
    if type(obj) == a_class:
        return True
    else:
        return False
