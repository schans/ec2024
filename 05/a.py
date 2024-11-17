#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append([int(c) for c in l.split()])


def dump(g):
    print('-'*22)
    for rr in g:
        print(' '.join([str(c) for c in rr]))
    print('-'*22)


Q = []
for i in range(len(G[0])):
    Q.append([r[i] for r in G])

R = 10
cols = len(G[0])

for r in range(R):
    cc = r % cols
    cr = (r+1) % cols
    claps = Q[cc].pop(0)
    crl = len(Q[cr])

    # 2 * full row, check in first or second half
    p = (claps - 1) % (2 * crl)
    if p > crl:
        # diff from back or row
        p = (crl * 2) - p

    Q[cr].insert(p, claps)

    print(r+1, ''.join([str(Q[i][0]) for i in range(cols)]))
