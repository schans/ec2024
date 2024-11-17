#!/usr/bin/env pypy3

import fileinput


G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append([c for c in l])
print(G)

next = (0, 0)
prev = (0, 0)
cur = (0, 1)
path = [G[0][1]]

rows = len(G)
cols = len(G[0])

while True:
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        rr, cc = cur
        rr += dr
        cc += dc
        if (rr, cc) == prev:
            continue
        if rr < 0 or cc < 0:
            continue
        if rr >= rows or cc >= len(G[rr]):
            continue

        print(rows, cols, dr, dc, rr, cc)
        if G[rr][cc] == ' ':
            continue

        path.append(G[rr][cc])
        next = (rr, cc)

    if path[-1] == 'S':
        break
    prev = cur
    cur = next

print(''.join(path))
