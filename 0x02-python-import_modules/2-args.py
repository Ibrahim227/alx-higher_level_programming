#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    pl = "s" if argc != 1 else ""
    print("{} argument{}{}{}".format(argc, pl, ":"if argc > 0 else ".", ""))
    for i, arg in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(i, arg))
