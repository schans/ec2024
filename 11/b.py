#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
DAYS = 10
R = dict()
P = ['Z']

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    p = l.split(':')
    R[p[0]] = p[1].split(',')

for _ in range(DAYS):
    NP = []
    for p in P:
        for n in R[p]:
            NP.append(n)
    P = NP


print(f"{len(P)}")
