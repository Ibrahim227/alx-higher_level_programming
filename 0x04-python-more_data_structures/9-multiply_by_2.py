#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    new_dict = list(a_dictionary.keys())
    for x in new_dict:
        new_dir[x] *= 2
    return (new_dir)
