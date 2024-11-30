#!/usr/bin/env pypy3

import fileinput
from collections import deque

S = (0, 0)
P = set()
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


def solve(start, height, points):
    q = deque()
    seen = set()
    prev = (-100, -100)
    q.append((0, height, start, prev, points))
    while q:
        (secs, h, cur,  prev, pi) = q.popleft()

        if cur == S and secs > 0 and h >= height and len(pi) == 0:
            return secs

        if (cur, h, pi) in seen:
            continue
        seen.add((cur, h, pi))

        for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = cur[0] + dr
            cc = cur[1] + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#' and (rr, cc) != prev:
                hh = h - 1
                if G[rr][cc] == '-':
                    hh -= 1
                elif G[rr][cc] == '+':
                    hh += 2

                pp = pi
                if pp and G[rr][cc] == pp[0]:
                    pp = pp[1:]

                q.append((secs+1, hh, (rr, cc), cur, pp))


mins = solve(S, 10000, 'ABC')

print('secs', mins)
