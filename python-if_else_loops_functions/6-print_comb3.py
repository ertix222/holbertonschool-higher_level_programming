#!/usr/bin/python3
for a in range(0, 100):
    if a // 10 < a % 10:
        if a != 89:
            print(f"{a:02d}, ", end="")
        else:
            print(f"{a}")
