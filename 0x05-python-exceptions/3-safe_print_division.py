#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{} / {} = {}".format(a, b, result))
    except ZeroDivisionError:
        return None
    finally:
        result = a / b
        print("Inside result: {}".format(result))
