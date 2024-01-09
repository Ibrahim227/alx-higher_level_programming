#!/usr/bin/python3
"""function definition """

def write_file(filename="", text=""):
    """writes a string to text file """
    with open("my_first_file.txt", "w", encoding="utf-8") as myfile:
        myfile.write(text)
