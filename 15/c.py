#!/usr/bin/env python3

import fileinput
from heapq import heappop, heappush
from itertools import permutations
from functools import cache

# counters
T = 0

S = E = (0, 0)
G = []
H = dict()

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append(l)
R = len(G)
C = len(G[0])

for c in range(C):
    if G[0][c] == '.':
        S = (0, c)
        break

for r in range(R):
    for c in range(C):
        if not G[r][c] in '.#~':
            if not G[r][c] in H:
                H[G[r][c]] = set()
            H[G[r][c]].add((r, c))


@cache
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
            if 0 <= rr < R and 0 <= cc < C and not G[rr][cc] in '#~':
                heappush(q, (d+1, (rr, cc)))

    assert False, "got lost in maze"


def route(start, end, visit):
    all = []
    for hperm in permutations(visit):
        # for hperm in perms:
        routes = [[start]]
        for hk in hperm:
            newroutes = []
            for h in H[hk]:
                for route in routes:
                    newroute = route.copy()
                    newroute.append(h)
                    newroutes.append(newroute)
            routes = newroutes
        all.extend(routes)

    mind = 1e6
    for route in all:
        curs = start
        dist = 0
        for nexts in route:
            dist += solve(min(curs, nexts), max(curs, nexts))
            curs = nexts
        dist += solve(curs, end)
        mind = min(mind, dist)

    # print('dist', start, end, visit, mind)
    return mind


#
dist = 0

# left, rigth E
RE = (75, 83)
dist += route(RE, RE, ['A', 'C', 'D'])
# right, left R
LR = (75, 171)
dist += route(LR, LR, ['N', 'P', 'Q'])
# middle
dist += route(S, S, ['G', 'I', 'J', 'E', 'R'])

print('dist', dist)
