#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = number % -10
elif number >= 0:
    ld = number % 10
if ld > 5:
    print(f"Last digit of {number} is {ls} and greater than 5")
if ld == 0: 
    print(f"Last digit of {number} is {ls} and is zero")
else:
    print(f"Last digit of {number} is {ld} and is zero")
