#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

N = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    N.append(int(l))

mi = min(N)
ma = max(N)


def count_level(l):
    t = 0
    for n in N:
        t += abs(n - l)
    return t


T = 1_000_000_000
for l in range(mi, ma):
    t = count_level(l)
    if t < T:
        T = t
    else:
        break

print(f"Tot {T}")
