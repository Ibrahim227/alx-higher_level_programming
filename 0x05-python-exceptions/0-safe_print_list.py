#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print("{}: {}".format(my_list[x], my_list.count))
    except:
        print("None")
