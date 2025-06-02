#!/usr/bin/python3
"""module to write a string in my_first_file.txt
"""


def write_file(filename="", text=""):
    """fonction that writes a string to a text file
    and return the number of characters
    """
    with open(filename, "w", encoding="UTF8") as file:
        content = file.write(text)
        return (content)
