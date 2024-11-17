#!/usr/bin/env python3

import fileinput

# counters
T = 0

G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append(l)


rows = len(G)
cols = len(G[0])


def dump(g):
    print('-'*22)
    for rr in g:
        print(rr)
    print('-'*22)


runes = []
for rr in range(rows):
    for cc in range(cols):
        if G[rr][cc] != '.':
            continue
        row = set(G[rr]) - set('.')
        col = set([G[i][cc] for i in range(cols)]) - set('.')
        runes.append((row & col).pop())

print(''.join(runes))
