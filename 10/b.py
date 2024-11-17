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


def dump(g):
    print('-'*22)
    for rr in g:
        print(rr)
    print('-'*22)


def get_runes(g):
    runes = []
    rows = len(g)
    cols = len(g[0])
    for rr in range(rows):
        for cc in range(cols):
            if g[rr][cc] != '.':
                continue
            row = set(g[rr]) - set('.')
            col = set([g[i][cc] for i in range(cols)]) - set('.')
            # print(rr, cc, row, col, row & col)
            runes.append((row & col).pop())
    return runes


def calc(rs):
    s = 0
    for i in range(len(rs)):
        s += (i+1)*(ord(rs[i])-64)
    return s


for sr in range(0, len(G), 8):
    for sc in range(0, len(G[0]), 9):
        sg = []
        for dr in range(8):
            rr = sr + dr
            sg.append([G[rr][sc+dc] for dc in range(8)])
        T += calc(get_runes(sg))

print(T)
