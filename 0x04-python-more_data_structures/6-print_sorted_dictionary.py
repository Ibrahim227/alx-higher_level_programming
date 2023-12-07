#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_ord = list(a_dictionary.keys())
    new_ord.sort()
    for i in new_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
