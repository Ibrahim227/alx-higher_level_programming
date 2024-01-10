#!/usr/bin/python3
""" Defines function"""


def lookup(obj):
    """ returns the list of\
        of available attr"""
    print(obj.__dict__, end="")
