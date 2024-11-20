#!/usr/bin/env pypy3

import fileinput

T = []

rows = 0
rr = 0
P = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for cc, c in enumerate(l):
        if c == 'A':
            P.append((rr, cc, 1))
        elif c == 'B':
            P.append((rr, cc, 2))
        elif c == 'C':
            P.append((rr, cc, 3))
        elif c == 'T':
            T.append((rr, cc, 1))
        elif c == 'H':
            T.append((rr, cc, 2))

    rr += 1
rows = rr


def can_hit(p, t) -> int:
    row_diff = t[0] - p[0]
    col_target = t[1] - row_diff
    can_hit = ((col_target-p[1]) % 3 == 0)
    pow = (col_target - p[1]) // 3
    score = pow * p[2] * t[2]
    if can_hit:
        return score
    else:
        return 0


s = []
for t in sorted(T):
    for p in P:
        s.append(can_hit(p, t))

print(f"Tot {sum(s)}")
