#!/usr/bin/env python3

import fileinput
from heapq import heappop, heappush
# counters
T = 0

S = E = (0, 0)
G = []
H = set()

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append(l)
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'H':
            H.add((r, c))


def solve(start, end):
    q = list()
    seen = set()
    q.append((0, start))
    while q:
        d, (r, c) = heappop(q)

        if (r, c) == end:
            return d

        if (r, c) in seen:
            continue
        seen.add((r, c))

        for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#':
                heappush(q, (d+1, (rr, cc)))

    assert False, "got lost in maze"


for c in range(C):
    if G[0][c] == '.':
        S = (0, c)
        break

mind = 1e6
for h in H:
    d = 2 * solve(S, h)
    mind = min(mind, d)
print('dist', mind)
