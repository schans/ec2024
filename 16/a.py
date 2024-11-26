#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
N = 0
S = []
R = []
for line in fileinput.input():
    # l = line.strip()
    l = line
    if not l.strip():
        continue

    if fileinput.lineno() == 1:
        S = [int(c) for c in l.split(',')]
        N = len(S)
        for _ in range(N):
            R.append([])
    else:
        for c in range(N):
            v = l[4*c:4*c+3]
            if v.strip():
                R[c].append(l[4*c:4*c+3])

P = [0 for _ in range(N)]
L = [len(R[c]) for c in range(N)]

for c in range(N):
    print(R[c][(S[c]*100) % L[c]], end=" ")
print()
