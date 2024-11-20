#!/usr/bin/env pypy3

import fileinput

C = {}
T = []
P = [(1, 1, 1), (2, 1, 2), (3, 1, 3)]
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    (c, r) = l.split()
    T.append((int(r), int(c)))


def calc_cache(p, max_power):
    for pow in range(max_power, 0, -1):
        (rr, cc, pp) = p
        t = 0
        # up
        for _ in range(pow):
            rr += 1
            cc += 1
            t += 1
            C[(rr, cc)] = (pow * pp, t)

        # right
        for _ in range(pow):
            cc += 1
            t += 1
            C[(rr, cc)] = (pow * pp, t)

        # down
        while rr > 1:
            rr -= 1
            cc += 1
            t += 1
            C[(rr, cc)] = (pow * pp, t)


def find_hit_score(p):
    (rr, cc) = p
    hits = []
    t = 0
    while rr > 0:
        if (rr, cc) in C:
            if C[(rr, cc)][1] <= t+1:
                hits.append((rr, C[(rr, cc)][0]))
        t += 1
        rr -= 1
        cc -= 1
    assert len(hits) > 0, "no hit??"
    return max(hits)[1]


maxp = max(T)[0]
calc_cache(P[2], maxp)
calc_cache(P[1], maxp)
calc_cache(P[0], maxp)

s = []
for t in T:
    s.append(find_hit_score(t))

print(f"Tot {sum(s)}")
