#!/usr/bin/env pypy3

import fileinput
from collections import Counter
from functools import cache


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


@cache
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


def next_states(p: tuple) -> list[tuple]:
    s = []
    s.append(next(back(p)))
    s.append(next(p))
    s.append(next(forward(p)))
    return s


@cache
def back(p: tuple):
    return tuple((c - 1) % L[i] for i, c in enumerate(p))


@cache
def forward(p: tuple):
    return tuple((c + 1) % L[i] for i, c in enumerate(p))


@cache
def next(p: tuple):
    return tuple((c + S[i]) % L[i] for i, c in enumerate(p))


def row(p: tuple) -> str:
    return ' '.join([R[i][c] for i, c in enumerate(p)])


p = tuple(P)

# calc max coins
keep = 1_000  # some large number..
maxs = 0
seen = set()
cur = p
prev_cand = [(0, p)]
for i in range(256):
    next_cand = []
    j = 0
    while prev_cand and j < keep:
        j += 1
        sc, st = prev_cand.pop()
        if (sc, st) in seen:
            continue
        seen.add((sc, st))
        ns = next_states(st)
        for s in ns:
            next_cand.append((score(s)+sc, s))
    prev_cand = sorted(next_cand)

maxs = max(prev_cand)[0]

# calc min coins
mins = 0
seen = set()
cur = p
prev_cand = [(0, p)]
for i in range(256):
    next_cand = []
    for sc, st in prev_cand:
        if st in seen:
            continue
        seen.add(st)

        ns = next_states(st)
        mins = min(prev_cand)[0]
        for s in ns:
            nsc = sc + score(s)
            next_cand.append((score(s)+sc, s))
    prev_cand = sorted(next_cand)

mins = min(prev_cand)[0]

print(f"Tot {maxs} {mins}")
