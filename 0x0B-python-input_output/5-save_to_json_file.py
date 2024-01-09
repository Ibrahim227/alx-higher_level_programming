#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """writes an obj to a text file"""
    with open("my_list.json", "w+") as myfile:
        
