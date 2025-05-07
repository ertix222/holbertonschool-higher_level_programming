#!/usr/bin/python3
for a in range(0, 89):
    if (a // 10 != a % 10) and (a // 10 < a % 10):
        print(f"{a:02d}, ".format(chr(a)), end="")
