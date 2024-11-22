#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

D = []
curx = cury = curz = 0
maxx = 0
P = set()

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    D = l.split(',')

for d in D:
    if d.startswith('U'):
        curx += int(d[1:])
    elif d.startswith('D'):
        curx -= int(d[1:])
    elif d.startswith('R'):
        cury += int(d[1:])
    elif d.startswith('L'):
        cury -= int(d[1:])
    elif d.startswith('F'):
        curz += int(d[1:])
    elif d.startswith('B'):
        curz -= int(d[1:])
    maxx = max(maxx, curx)
    P.add((curx, cury, curz))


print(f"Tot {maxx}")
