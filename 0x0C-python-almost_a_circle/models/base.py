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
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if not list_objs:
            
