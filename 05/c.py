#!/usr/bin/env pypy3

import fileinput

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


def get_q_set(q):
    s = []
    for j in range(len(q)):
        s.append(int(''.join([str(c) for c in q[j]])))
    return tuple(s)


R = 100_000_000_000

mn = 0
cols = len(G[0])

seen = {}
seenq = set()

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

    # accounting
    num = int(''.join([str(Q[i][0]) for i in range(cols)]))
    if num in seen:
        seen[num] += 1
    else:
        seen[num] = 1

    mn = max(mn, num)
    qs = get_q_set(Q)
    if qs in seenq:
        print('step', r+1, 'max', mn)
        break
    seenq.add(qs)
