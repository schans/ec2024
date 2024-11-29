#!/usr/bin/env pypy3

import fileinput
from copy import deepcopy

# counters
T = 0
N = 0
DR = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
DL = DR[::-1]

MARK = '%'
P = set()
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
OG = deepcopy(G)

for c in range(C):
    for r in range(R):
        if G[r][c] in '><123456789':
            P.add((r, c))


def rotate(d, p, pi):

    if d == 'R':
        D = DR
    elif d == 'L':
        D = DL
    else:
        assert False, f"unknown dir {d=}"

    (r, c) = p
    prev = G[r+D[-1][0]][c+D[-1][1]]
    for dr, dc in D:
        cur = G[r+dr][c+dc]
        G[r+dr][c+dc] = prev
        if prev == MARK:
            pi = (r+dr, c+dc)
        prev = cur

    return pi


def final_dest(pi):
    global G, OG
    seen = set()
    pos = list()

    rounds = 1048576000
    G[pi[0]][pi[1]] = MARK

    for j in range(rounds):
        i = 0
        if pi in seen:
            G = deepcopy(OG)  # reset
            return pos[rounds % j]

        seen.add(pi)
        pos.append(pi)

        for r in range(1, R-1):
            for c in range(1, C-1):
                d = I[i % N]
                for dr, dc in DR:
                    if G[r+dr][c+dc] in '%':
                        pi = rotate(d, (r, c), pi)
                        break
                i += 1


solution = {}
for p in P:
    pos = final_dest(p)
    # print('found', pos, G[p[0]][p[1]])
    solution[pos] = G[p[0]][p[1]]
print(''.join([solution[p] for p in sorted(solution.keys())]))
