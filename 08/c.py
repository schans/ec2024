#!/usr/bin/env pypy3


T = 0
npe = 969217
acco = 10
blocks = 202400000


tower = 1
pprev = 0
prev = 1
heights = [1]

for width in range(3, 1_000_000, 2):
    thick = (prev * npe) % acco + acco
    tower += (thick * width)
    for i in range(len(heights)):
        heights[i] += thick

    # carve
    carve = 0
    for i in range(len(heights)):
        carve += ((npe * width) * heights[i]) % acco
        if i > 0:
            carve += ((npe * width) * heights[i]) % acco

    heights.append(thick)
    pprev = prev
    prev = thick

    if (tower-carve) > blocks:
        T = (tower - blocks - carve)
        break

print(f"Tot {T}")
