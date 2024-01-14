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
        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if not list_objs:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)
