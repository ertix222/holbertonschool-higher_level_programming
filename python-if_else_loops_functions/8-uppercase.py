#!/usr/bin/python3
def uppercase(str):
    for c in str:
        value = ord(c)
        if (ord(c) in range(97, 123)):
            value = value - 32
        print("{}".format(chr(value)), end="")
    print("")
