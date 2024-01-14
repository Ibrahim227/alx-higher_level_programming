#!/usr/bin/python3
"""Modules Documentation"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        list_dictionaries = ['x', 'width', 'id', 'height', 'y']
        if list_dictionaries is None or list_dictionaries == []:
            print("[]")
        return json.dumps(list_dictionaries)
