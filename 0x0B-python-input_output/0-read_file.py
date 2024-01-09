#!/usr/bin/python3
""" function Definition"""


def read_file(filename=""):
    """ reads a text file """
    with open('my_file_0.txt', "r") as f:
        res = f.read()
        print(res, end="")
