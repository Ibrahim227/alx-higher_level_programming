#!/usr/bin/python3
"""Modules Documentation"""
import json
import csv


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
            tr = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(tr)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string, object_pairs_hook=dict)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsoported class for create method")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Defines a function that save file to csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        """defines function to load from csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            instance = []
            for row in csv_reader:
                instance = cls.from_csv(row)
                instances.append(instance)
            return instances
        except FileNotFoundError:
            return []
