#!/usr/bin/env python3

import fileinput
from heapq import heappop, heappush

S = E = (0, 0)
G = []

P = set()

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append(l)
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'P':
            P.add((r, c))


for c in range(C):
    if G[0][c] == '.':
        S = (0, c)
        break
    if G[R-1][c] == '.':
        S = (R-1, c)


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


times = []
for p in P:
    times.append(solve(S, p))

print('time', max(times)-1)
