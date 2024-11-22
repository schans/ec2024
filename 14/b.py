#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

D = []
P = set()

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


print(f"Tot {len(P)}")
