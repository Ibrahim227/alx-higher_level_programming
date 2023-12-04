#!/usr/bin/python3
def replace_int_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    new_element = element
    my_list[idx] = new_element
    return my_list
