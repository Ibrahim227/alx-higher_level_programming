#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
    #print("Element at {:d} is {}".format(idx, elemet_at(my_list, idx)))
