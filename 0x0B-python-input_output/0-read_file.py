#!/usr/bin/python3
""" function Definition"""


def read_file(filename=""):
    """ reads a text file """
    with open(filename='my_file_0.txt', 'r', encoding='utf-8') as f:
        f.read()
