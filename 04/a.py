#!/usr/bin/env python3

import fileinput

# counters
T = 0

N = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    N.append(int(l))

m = min(N)
for n in N:
    T += n - m

print(f"Tot {T}")
