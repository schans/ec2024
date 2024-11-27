#!/usr/bin/env python3

import fileinput
from heapq import heappop, heappush
from collections import deque
# counters
T = 0

S = E = (0, 0)
G = []
S = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append(l)
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == '*':
            S.append((r, c))


def manh(p1, p2) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


dists = []
for i in range(len(S)):
    for j in range(i+1, len(S)):
        dists.append((manh(S[i], S[j]), i, j))
dists = deque(sorted(dists))


def find_min(dists):
    seen = set()
    dist, fr, to = dists.popleft()
    paths = [(fr, to)]
    total = dist
    seen.add(fr)
    seen.add(to)
    while len(seen) < len(S):
        for can_dist, can_fr, can_to in dists:
            if can_fr in seen and can_to in seen:
                continue
            if can_fr in seen or can_to in seen:
                seen.add(can_to)
                seen.add(can_fr)
                total += can_dist
                paths.append((can_fr, can_to))
                dists.remove((can_dist, can_fr, can_to))
                break

    assert len(seen) == len(S)
    return total


T = find_min(dists) + len(S)
print(f"{T=}")
