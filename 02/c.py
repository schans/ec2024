#!/usr/bin/env pypy3

import fileinput

F = set()

ls = [line.strip() for line in fileinput.input()]


words = ls[0].split(':')[1].split(',')
lines = ls[2:]

rows = len(lines)
cols = len(lines[0])

rr = 0
for line in lines:
    lm = 0
    dl = line+line
    for i in range(cols):
        for w in words:
            if dl[i:].startswith(w) or dl[i:].startswith(w[::-1]):
                e = i + len(w)
                if lm < e:
                    for cc in range(max(i, lm), e):
                        F.add((rr, cc % cols))
                    lm = e
    rr += 1

trans = []
for i in range(cols):
    trans.append(''.join([line[i] for line in lines]))

cc = 0
for tran in trans:
    lm = 0
    dl = tran  # don't loop
    for i in range(rows):
        for w in words:
            if dl[i:].startswith(w) or dl[i:].startswith(w[::-1]):
                e = i + len(w)
                if lm < e:
                    for rr in range(max(i, lm), e):
                        F.add((rr % rows, cc))
                    lm = e
    cc += 1

print(f"Tot {len(F)}")
