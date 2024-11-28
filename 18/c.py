#!/usr/bin/env python3

import fileinput

S = set()
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
        if G[r][c] == '.':
            S.add((r, c))


def fill(s):
    ps = P.copy()
    t = 0
    times = []
    seen = set()
    heads = set()
    heads.add(s)
    seen.add(s)
    while ps:
        t += 1
        newheads = set()
        for (r, c) in heads:
            for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != '#' and (rr, cc) not in seen:
                    newheads.add((rr, cc))
                    seen.add((rr, cc))
                    if (rr, cc) in ps:
                        ps.remove((rr, cc))
                        times.append(t)
        heads = newheads
    return sum(times)


mint = 1e8
for s in S:
    t = fill(s)
    mint = min(mint, t)

print('time', mint)
