#!/usr/bin/env python3

import fileinput
from heapq import heappop, heappush

E = (0, 0)
G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append(l)
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'E':
            E = (r, c)


def dump(g):
    print('-'*22)
    for rr in g:
        print(rr)
    print('-'*22)


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
            if 0 <= rr < R and 0 <= cc < C and not G[rr][cc] in 'S#' and not (rr, cc) in seen:
                h = G[r][c]
                hh = G[rr][cc]
                if h in 'SE':
                    h = 0
                else:
                    h = int(h)
                if hh in 'SE':
                    hh = 0
                else:
                    hh = int(hh)

                dd = d + 1 + min(abs(h - hh), abs(h - hh - 10), abs(h-hh+10))
                heappush(q, (dd, (rr, cc)))

    # assert False, "got lost in maze"
    # not every start point is guarnteed to have a solution
    return 1e6


mins = 1e6
for r in range(1, R-1):
    s = solve((r, 0), E)
    mins = min(mins, s)
    s = solve((r, C-1), E)
    mins = min(mins, s)

for c in range(1, C-1):
    s = solve((0, c), E)
    mins = min(mins, s)
    s = solve((R-1, c), E)
    mins = min(mins, s)

print('time', mins)
