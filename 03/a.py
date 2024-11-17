#!/usr/bin/env python3

import fileinput

# counters
T = 0

G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    rr = []
    for c in l:
        if c == '#':
            rr.append(1)
        else:
            rr.append(0)

    G.append(rr)


def dump(g):
    print('-'*22)
    for rr in g:
        print(''.join([str(c) for c in rr]).replace('0', '.'))
    print('-'*22)


lm = 0
nm = 1

rows = len(G)
cols = len(G[0])

while nm != lm:
    lm = nm
    for cc in range(1, cols-1):
        for rr in range(1, rows-1):
            if G[rr][cc] != 0 and \
                    0 <= G[rr-1][cc] - lm <= 1 and \
                    0 <= G[rr+1][cc] - lm <= 1 and \
                    0 <= G[rr][cc-1] - lm <= 1 and \
                    0 <= G[rr][cc+1] - lm <= 1:
                G[rr][cc] = lm + 1
                nm = lm + 1


for rr in G:
    T += sum(rr)
print(f"Tot {T}")
