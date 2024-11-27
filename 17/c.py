#!/usr/bin/env python3

import fileinput
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
        dist = manh(S[i], S[j])
        if dist < 6:
            dists.append((dist, i, j))
dists = deque(sorted(dists))


def find_min(dists):
    dists_len = len(dists)
    seen = set()
    dist, fr, to = dists.popleft()
    paths = [(fr, to)]
    total = dist
    seen.add(fr)
    seen.add(to)
    found = True
    while len(seen) < len(S) and found:
        found = False
        for can_dist, can_fr, can_to in dists:
            if can_fr in seen and can_to in seen:
                continue
            if can_fr in seen or can_to in seen:
                seen.add(can_to)
                seen.add(can_fr)
                total += can_dist
                paths.append((can_fr, can_to))
                found = True
                dists.remove((can_dist, can_fr, can_to))
                break

    assert len(dists) + len(paths) == dists_len
    return total + len(seen), seen


sizes = []
while dists:
    t, seen = find_min(dists)
    sizes.append(t)
    # filter dists for seen stars
    new_dists = deque()
    for dist, fr, to in dists:
        if fr in seen or to in seen:
            continue
        new_dists.append((dist, fr, to))
    dists = new_dists

sizes = sorted(sizes)
T = sizes[-1] * sizes[-2] * sizes[-3]
print(f"{T=}")
