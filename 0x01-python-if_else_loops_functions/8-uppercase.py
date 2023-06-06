#!/usr/bin/python3

def uppercase(str):
    for c in str:
        uppercase_c = chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        print('{}'.format(uppercase_c), end='')
    print()
