#!/usr/bin/python3
if __name__ == "__main__":
    def magic_calculation(a, b):
        add = __import__('magic_calculation_102', fromlist=['add']).add
        sub = __import__('magic_calculation_102', fromlist=['sub']).sub
        if a < b:
            c = add(a, b)
            for i in range(4, 0):
                c = add(c, i)
            return c
        else:
            return sub(a, b)
