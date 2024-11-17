#!/usr/bin/env pypy3

import fileinput
from itertools import permutations

TR = 'S+=+++===-+++++=-==+--+=+===-++=====+--===++=-==+=++====-==-===+=+=--==++=+========-=======++--+++=-++=-+=+==-=++=--+=-====++--+=-==++======+=++=-+==+=-==++=-=-=---++=-=++==++===--==+===++===---+++==++=+=-=====+==++===--==-==+++==+++=++=+===--==++--===+=====-=++====-+=-+--=+++=-+-===++====+++--=++====+=-=+===+=====-+++=+==++++==----=+=+=-'

R = {}
N = 0
S = {}

segl = 1

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    r, p = l.split(':')
    R[r] = p.split(',')
    segl = len(R[r])
    S[r] = []
    # break


def calc(plan):
    pows = []
    for n in range(0, 2024 * len(TR)):
        t = TR[(n+1) % len(TR)]

        if n == 0:
            pow = 10
        else:
            pow = pows[n-1]

        if t == '+':
            pows.append(pow+1)
        elif t == '-':
            pows.append(pow-1)
        elif plan[n % len(plan)] == '+':
            pows.append(pow+1)
        elif plan[n % len(plan)] == '-':
            pows.append(pow-1)
        else:
            pows.append(pow)

    return pows


to_beat = sum(calc(R['A']))

print("beat", to_beat)

wins = 0

perm = permutations(['=', '=', '=', '-', '-', '-', '+', '+', '+', '+', '+'])
for p in set(perm):
    s = sum(calc(p))
    if s > to_beat:
        wins += 1

print('wins', wins)
