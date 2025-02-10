#!/usr/bin/python3
def read_file(filename=""):
    """
    defines a fonction that read text file
    """
    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)