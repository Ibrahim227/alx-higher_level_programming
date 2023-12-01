#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for t in name:
        if t[:2] != "__":
            print(t)
