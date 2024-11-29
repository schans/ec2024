#!/usr/bin/env pypy3

import fileinput

# counters
N = 0
DR = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
DL = DR[::-1]
I = []
G = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    if fileinput.lineno() == 1:
        N = len(l)
        I = list(l)
    else:
        G.append(list(l))

R = len(G)
C = len(G[0])


def dump():
    for r in range(R):
        print(''.join(G[r]))


def rotate(d, r, c):
    if d == 'R':
        D = DR
    elif d == 'L':
        D = DL
    else:
        assert False, f"unknown dir {d=}"

    prev = G[r+D[-1][0]][c+D[-1][1]]
    for dr, dc in D:
        cur = G[r+dr][c+dc]
        G[r+dr][c+dc] = prev
        prev = cur


for _ in range(100):
    i = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            d = I[i % N]
            rotate(d, r, c)
            i += 1

dump()
