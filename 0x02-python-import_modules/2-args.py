#!/usr/bin/python3
if __name__ == "__main__":
    """import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
    else:
        print("{} arguments".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))"""
    from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    plural_s = "s" if argc != 1 else ""
    print("{} argument{}{}{}".format(argc, plural_s, ":"if argc > 0 else ".", ""))
    for i, arg in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(i, arg))
