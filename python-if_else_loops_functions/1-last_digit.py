#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgt_nbr = abs(number) % 10
if number < 0:
    dgt_nbr = -dgt_nbr

if dgt_nbr > 5:
    print(f"Last digit of {number} is {dgt_nbr} and is greater than 5")
elif dgt_nbr < 6 and dgt_nbr != 0:
    print(f"Last digit of {number} is {dgt_nbr} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {dgt_nbr} and is 0")
