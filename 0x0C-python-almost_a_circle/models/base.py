#!/usr/bin/python3
"""Modules Documentation"""


class Base:
    """Define new class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Define the construtor"""
        self.id = id

        if id is not None:
            id = self.id
        else:
            __nb_objects += 1
            self.id = __nb_objects   
