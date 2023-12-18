#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except TypeError:
        return False
    except ValueError as e:
        print("Unknown format code 'd' for object of type 'str'")
