#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
DAYS = 20

R = dict()
minr = 1e12
maxr = 0

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    p = l.split(':')
    R[p[0]] = p[1].split(',')

for s in R:
    P = {s: 1}
    for _ in range(DAYS):
        NP = dict()
        for p in P:
            for n in R[p]:
                if n in NP:
                    NP[n] += P[p]
                else:
                    NP[n] = P[p]
        P = NP
    psum = sum(P.values())
    minr = min(minr, psum)
    maxr = max(maxr, psum)

print(f"{maxr - minr}")
