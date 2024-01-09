#!/usr/bin/python3
""" function Definition"""


def read_file(filename=""):
    """ reads a text file """
    with open(filename, encoding="utf-8") as f:
        res = f.read()
        print(res, end="")
