#!/usr/bin/env pypy3


T = 0

blocks = 4097874

tower = 0
for i in range(1, 1_000_000, 2):
    tower += i
    if tower > blocks:
        T = (tower - blocks) * i
        break

print(f"Tot {T}")
