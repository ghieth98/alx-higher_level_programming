#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if number < 0:
    last_number *= -1
if last_number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_number))
if last_number == 0:
    print("Last digit of {} is 0 and is 0".format(number))
if last_number < 6 and last_number != 0:
    print("last digit of {} is {} and is less than 6 and not 0".format(number, last_format))

