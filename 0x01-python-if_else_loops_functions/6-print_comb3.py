#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        print('{:d}{:d}'.format(i, y), end=', ' if i < 8 or y < 9 else '\n')
