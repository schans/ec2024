#!/usr/bin/env python3

import fileinput

# counters
T = 0

G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    G.append([c for c in l])


def dump(g):
    print('-'*22)
    for rr in g:
        print(''.join(rr))
    print('-'*22)


def fill_runes(sr, sc):
    rows = 8
    cols = 8

    # direct fills
    for rr in range(sr, sr+rows):
        for cc in range(sc, sc+cols):
            if G[rr][cc] != '.':
                continue
            row = set([G[rr][i] for i in range(sc, sc + cols)]) - set('.')
            col = set([G[i][cc] for i in range(sr, sr + rows)]) - set('.')
            cr = row & col
            if len(cr) == 0:
                G[rr][cc] = '.'
            elif len(cr) == 1:
                G[rr][cc] = cr.pop()
            else:
                # assert False, cr
                # cannot fill
                return

    # find possible '?' fills
    for rr in range(sr, sr+rows):
        for cc in range(sc, sc+cols):
            if G[rr][cc] != '.':
                continue
            row = [G[rr][i] for i in range(sc, sc + cols)]
            col = [G[i][cc] for i in range(sr, sr + rows)]

            # complete row if no '?'
            if not '?' in row:
                seen = set()
                for c in row:
                    if c == '.':
                        continue
                    if c in seen:
                        seen.remove(c)
                    else:
                        seen.add(c)
                if len(seen) == 1:
                    G[rr][cc] = seen.pop()
                    for i in range(sr, sr+rows):
                        if G[i][cc] == '?':
                            G[i][cc] = G[rr][cc]
                else:
                    # assert False, seen
                    # cannot fill
                    return

            # complete col if no '?'
            if not '?' in col:
                seen = set()
                for c in col:
                    if c == '.':
                        continue
                    if c in seen:
                        seen.remove(c)
                    else:
                        seen.add(c)
                if len(seen) == 1:
                    G[rr][cc] = seen.pop()
                    for i in range(sc, sc+cols):
                        if G[rr][i] == '?':
                            G[rr][i] = G[rr][cc]
                else:
                    # assert False, seen
                    # cannot fill
                    return

# get inner runes


def get_runes(sr, sc):
    runes = []
    rows = 8
    cols = 8
    for rr in range(sr+2, sr+rows-2):
        for cc in range(sc+2, sc+cols-2):
            runes.append(G[rr][cc])
    assert len(runes) == 16, len(runes)
    return runes

# calc rune score if all filled


def calc(rs):
    s = 0
    for i in range(len(rs)):
        # check unfilled
        if rs[i] == '.':
            return 0
        s += (i+1)*(ord(rs[i])-64)
    return s


# couple of iterations to settle
for _ in range(10):
    for sr in range(0, len(G)-6, 6):
        for sc in range(0, len(G[0])-6, 6):
            fill_runes(sr, sc)

# calc score
for sr in range(0, len(G)-6, 6):
    for sc in range(0, len(G[0])-6, 6):
        runes = get_runes(sr, sc)
        T += calc(runes)

print(T)
