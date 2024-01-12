#!/usr/bin/python3
"""Modules Documentation"""


class Base:
    """Define new class Base"""
    def __init__(self, id=None):
        """Define the construtor"""
        self.id : int = id
        __nb_objects = 0

        if id is not None:
            id = self.id
        __nb_objects += 1
        self.id = __nb_objects   
