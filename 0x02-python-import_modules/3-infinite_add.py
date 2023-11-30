#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cal = 0
    for i in range(len(sys.argv) - 1):
        cal += int(sys.argv[i + 1])
        print("{}".format(cal))
