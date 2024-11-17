#!/usr/bin/env pypy3

import fileinput
from functools import cache

# counters
T = 0

sparks = []

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

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


def min_couple(amount):
    low = amount // 2 + amount % 2 - 50
    btls = []
    for i in range(low, amount//2 + 1 + amount % 2):
        btls.append(min_beetles(i) + min_beetles(amount-i))
    return min(btls)


# populate cache
for spark in range(max(sparks)):
    min_beetles(spark)

for spark in sparks:
    T += min_couple(spark)

print(f"Tot {T}")
