#!/usr/bin/env python3

import fileinput

# counters
T = 0


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for cs in range(0, len(l), 2):
        pair = True
        for c in l[cs:cs+2]:
            if c == 'B':
                T += 1
            elif c == 'C':
                T += 3
            elif c == 'D':
                T += 5
            elif c == 'x':
                pair = False
        if pair:
            T += 2

print(f"Tot {T}")
