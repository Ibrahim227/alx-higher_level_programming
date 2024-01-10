#!/usr/bin/python3
"""Defines an obj from json"""
import json


def load_from_json_file(filename):
    """creates an obj from a json file"""
    with open(filename) as f:
        return json.load(f)
