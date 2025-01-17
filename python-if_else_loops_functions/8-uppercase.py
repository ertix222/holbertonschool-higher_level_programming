#!/usr/bin/python3
def uppercase(str):
    for c in str:
        value = ord(c)
        if (ord(c) in range(97, 123)):
            c = chr(ord(c) - 32)
        print("{}".format(chr(c)), end="")
    print("")
