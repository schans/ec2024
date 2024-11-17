#!/usr/bin/env pypy3


T = 0


npe = 547
acco = 1111
blocks = 20240000


tower = 1
prev = 1
for i in range(3, 1_000_000, 2):
    thick = (prev * npe) % acco
    prev = thick
    tower += (thick * i)
    if tower > blocks:
        T = (tower - blocks) * i
        break

print(f"Tot {T}")
