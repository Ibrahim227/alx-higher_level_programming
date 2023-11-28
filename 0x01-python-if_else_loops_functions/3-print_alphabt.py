#!/usr/bin/python3
for let in range(ord('a'), ord('z') + 1):
    if chr(let) not in ['e', 'q']:
        print("{}".format(chr(let)), end='')
