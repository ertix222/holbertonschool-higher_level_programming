#!/usr/bin/python3
"""module to read the file my_file_0.txt
"""


def read_file(filename=""):
    """fonction that read and print a text file
    """
    with open(filename, "r", encoding="UTF8") as file:
        content = file.read()
        print(content, end="")
