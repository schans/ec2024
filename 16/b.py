#!/usr/bin/env pypy3

import fileinput
from collections import Counter

# counters
T = 0
N = 0
S = []
R = []
for line in fileinput.input():
    # l = line.strip()
    l = line
    if not l.strip():
        continue

    if fileinput.lineno() == 1:
        S = [int(c) for c in l.split(',')]
        N = len(S)
        for _ in range(N):
            R.append([])
    else:
        for c in range(N):
            v = l[4*c:4*c+3]
            if v.strip():
                R[c].append(l[4*c:4*c+3])

P = [0 for _ in range(N)]
L = [len(R[c]) for c in range(N)]

SS = dict()
RSS = dict()


def score(p: tuple) -> int:
    rs = 0
    chrs = []
    for c in range(N):
        chrs.extend(list(R[c][p[c]]))
    # print(i, chs, Counter(chs))
    for (v, cnt) in Counter(chrs).items():
        if cnt >= 3 and v not in ".,:;_":
            rs += (cnt-2)
    return rs


def period_score(runs: int):
    s = 0
    for i in range(1, runs):
        for c in range(N):
            P[c] = (i * S[c]) % L[c]
        rs = score(tuple(P))
        s += rs
        RSS[s] = i
        SS[i] = s
        if sum(P) == 0 and i > 0:
            return i, s

    assert False, "not found"


ps = []
for c in range(N):
    ps.append(S[c]*L[c])
period, pscore = period_score(100_000)
# print(f'{period=} {pscore=}')

pulls = 202420242024
rounds = pulls // period
coins = rounds * pscore
left = pulls - (rounds*period)
coins += SS[left]
print(f"{pulls=} {coins=}")
