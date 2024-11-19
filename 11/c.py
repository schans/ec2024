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

print(R)

for s in R.keys():
    P = dict()
    P[s] = 1
    for _ in range(DAYS):
        NP = dict()
        for p in P.keys():
            for n in R[p]:
                if n in NP:
                    NP[n] = NP[n] + P[p]
                else:
                    NP[n] = P[p]
                # print(f'{p=} {n=} {NP[n]=}')
        P = NP
        print(P)
    psum = sum([P[p] for p in P])
    minr = min(minr, psum)
    maxr = max(maxr, psum)
    print(minr, maxr)

print(f"{maxr - minr}")
