#!/usr/bin/python3
def append_write(filename="", text=""):
    """ Appends a string to the end of file """
    with open("file_append.txt", "w") as myfile:
        myfile.write("This School is so cool!\n")
    with open("file_append.txt", "a") as myfile:
        myfile.write("This School is so cool!\n")
