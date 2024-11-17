#!/usr/bin/env pypy3

import fileinput

# TR = 'S+===++-=+=-'
TR = 'S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=---=++==--+++==++=+=--==++==+++=++=+++=--=+=-=+=-+=-+=-+-=+=-=+=-+++=+==++++==---=+=+=-'

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


for n in range(0, 10 * len(TR)):
    t = TR[(n+1) % len(TR)]
    for r, p in R.items():
        if n == 0:
            pow = 10
        else:
            pow = S[r][n-1]

        if t == '+':
            S[r].append(pow+1)
        elif t == '-':
            S[r].append(pow-1)
        elif p[n % segl] == '+':
            S[r].append(pow+1)
        elif p[n % segl] == '-':
            S[r].append(pow-1)
        else:
            S[r].append(pow)

SS = dict()
for r, ps in S.items():
    SS[r] = sum(ps)


print(''.join([k for k, v in sorted(SS.items(), reverse=True, key=lambda item: item[1])]))
