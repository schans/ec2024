#!/usr/bin/env pypy3

import fileinput
from collections import deque

S = E = (0, 0)
G = []
S = ()

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append(l)
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            S = (r, c)


def solve(start, height, secs):
    q = deque()
    seen = set()
    prev = (-100, -100)
    q.append((height, secs, start, prev))
    maxh = 0
    while q:
        h, secs, (r, c),  prev = q.pop()

        if secs == 0:
            maxh = max(maxh, h)
            continue

        if (h, secs, (r, c)) in seen:
            continue
        seen.add((h, secs, (r, c)))

        for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#' and (rr, cc) != prev:
                hh = h - 1
                if G[rr][cc] == '-':
                    hh -= 1
                elif G[rr][cc] == '+':
                    hh += 2
                q.append((hh, secs - 1, (rr, cc), (r, c)))

    return maxh


maxh = solve(S, 1000, 100)

print('height', maxh)
