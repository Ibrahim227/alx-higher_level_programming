#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return map([lambda x: x * number for x in my_list], my_list)
