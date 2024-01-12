#!/usr/bin/python3
"""Modules Documentation"""


class Base:
    """Define new class Base"""
    __nb_objects = 0  # privae calsse attribute

    def __init__(self, id=None):
        """Define the construtor"""
        self.id: int = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
