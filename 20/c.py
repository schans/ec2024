#!/usr/bin/env pypy3

import fileinput
from heapq import heappop, heappush

S = (0, 0)
P = set()
G = []
S = (-1, -1)

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


# solve asc instead of desc
def solve(start, end):
    q = list()
    seen = set()
    prev = (-100, -100)
    heappush(q, (0, (start, prev)))
    while q:
        h, (cur,  prev) = heappop(q)

        if cur == end:
            return h

        if (cur, h) in seen:
            continue
        seen.add((cur, h))

        for (dr, dc) in [(0, 1), (1, 0), (0, -1)]:
            rr = cur[0] + dr
            cc = cur[1] + dc
            if rr >= 0 and 0 <= cc < C and G[rr % R][cc] != '#' and (rr, cc) != prev:
                hh = h + 1
                if G[rr % R][cc] == '-':
                    hh += 1
                elif G[rr % R][cc] == '+':
                    hh -= 2
                heappush(q, (hh, ((rr, cc), cur)))

    return 1e6


# find optimal paths through grid
startmin = endmin = (0, 0)
dropmin = 1000
can = []
for j in range(1, C-1):
    start = (0, j)
    end = (R, j)
    if G[0][j] == '#':
        continue

    drop = solve(start, end)
    if drop < dropmin:
        can = [j]
        dropmin = drop
    elif drop == dropmin:
        can.append(j)

# use optimal path closest to start
bestmin = min([(abs(S[1]-c), c) for c in can])[1]

starth = 384400

# travel to optimal part start point
firsttravel = R
firstdrop = solve(S, (firsttravel, bestmin))
travelled = firsttravel
starth -= firstdrop

# calc iters
iters = starth // dropmin
lefth = starth % dropmin

# check last for 0 in the grid
if lefth == 0:
    iters -= 1
    lefth += dropmin

travelled += iters * R

# last part in grid
for i in range(R):
    s = solve((0, bestmin), (i, bestmin))
    if s == lefth:
        extra = i
        travelled += i
        break

print('dist', travelled)
