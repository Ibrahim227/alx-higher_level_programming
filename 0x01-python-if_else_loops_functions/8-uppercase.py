#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if ord('a') <= ord(let) <= ord('z'):
            let = chr(ord(let) - 32)
        print("{:s}".foramt(let), end="")
    print()
