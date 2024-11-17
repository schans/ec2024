#!/usr/bin/env pypy3

import fileinput

# counters
T = 0


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for c in l:
        if c == 'B':
            T += 1
        elif c == 'C':
            T += 3

print(f"Tot {T}")
