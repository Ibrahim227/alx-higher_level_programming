#!/usr/bin/python3
def print_last_digit(number):
    if numbe < 0:
        ld = number % -10
    elif number >= 0:
        ld = number % 10
    print("{:}".format(ld), end="")
    return ld
