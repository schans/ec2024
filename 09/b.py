#!/usr/bin/env pypy3

import fileinput
from functools import cache

# counters
T = 0

sparks = []

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    sparks.append(int(l))


@cache
def min_beetles(amount):
    # zero coins for zero
    if amount == 0:
        return 0

    if amount < 0:
        assert False, "no good"

    btls = []
    for s in stamps:
        if s <= amount:
            btls.append(1 + min_beetles(amount - s))
    return min(btls)


# populate cache
for spark in range(max(sparks)):
    min_beetles(spark)

for spark in sparks:
    T += min_beetles(spark)


print(f"Tot {T}")
