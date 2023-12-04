#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in range(len(matrix)):
            for item in range(len(matrix[i])):
                if item != len(matrix[i] - 1):
                    esp = ''
                else:
                    esp = ''
                print("{:d}".format(matrix[i][item]), end=esp)
        print()
