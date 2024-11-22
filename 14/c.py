#!/usr/bin/env pypy3

import fileinput
from heapq import heappop, heappush

# counters
T = 0

D = []
P = set()
L = set()

maxx = 0

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    D.append(l.split(','))

for dd in D:
    curx = cury = curz = 0
    for d in dd:
        if d.startswith('U'):
            for _ in range(int(d[1:])):
                curx += 1
                P.add((curx, cury, curz))
        elif d.startswith('D'):
            for _ in range(int(d[1:])):
                curx -= 1
                P.add((curx, cury, curz))
        elif d.startswith('R'):
            for _ in range(int(d[1:])):
                cury += 1
                P.add((curx, cury, curz))
        elif d.startswith('L'):
            for _ in range(int(d[1:])):
                cury -= 1
                P.add((curx, cury, curz))
        elif d.startswith('F'):
            for _ in range(int(d[1:])):
                curz += 1
                P.add((curx, cury, curz))
        elif d.startswith('B'):
            for _ in range(int(d[1:])):
                curz -= 1
                P.add((curx, cury, curz))
    maxx = max(maxx, curx)
    L.add((curx, cury, curz))


def dump(x):
    print(x, '-'*22)
    for y in range(-5, 5):
        for z in range(-5, 5):
            if y == 0 and z == 0:
                print('*', end='')
            elif (x, y, z) in L:
                print('L', end='')
            elif (x, y, z) in P:
                print('X', end='')
            else:
                print('.', end='')
        print()
    print('-'*22)


def solve(start, end):
    q = list()
    seen = set()
    q.append((0, start))
    while q:
        d, (x, y, z) = heappop(q)

        if (x, y, z) == end:
            return d

        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))

        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            xx = x + dx
            yy = y + dy
            zz = z + dz
            if (x, y, z) in P:
                heappush(q, (d+1, (xx, yy, zz)))

    # assert False, "got lost in maze"
    # not every start point is guarnteed to have a solution
    return 1e6


minmurk = 1e6
for x in range(maxx):
    murk = 0
    for l in L:
        d = solve(l, (x, 0, 0))
        murk += d
    minmurk = min(minmurk, murk)


print(f"Tot {minmurk}")
