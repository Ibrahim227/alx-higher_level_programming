#!/usr/bin/python3
for num in range(0, 100):
    print("{:02d}".format(num), end=', ' if num < 100 else "\n")
