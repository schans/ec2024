#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

sparks = []

stamps = [10, 5, 3, 1]

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    sparks.append(int(l))

for spark in sparks:
    bs = 0
    for st in stamps:
        left = spark % st
        bs += spark // st
        spark = left
    T += bs

print(f"Tot {T}")
