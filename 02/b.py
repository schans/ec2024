#!/usr/bin/env python3

import fileinput
# counters
T = 0


ls = [line.strip() for line in fileinput.input()]


words = ls[0].split(':')[1].split(',')
lines = ls[2:]


for line in lines:
    lm = 0
    for i in range(len(line)):
        for w in words:
            if line[i:].startswith(w) or line[i:].startswith(w[::-1]):
                e = i + len(w)
                if lm < e:
                    T += (e - max(i, lm))
                    lm = e

print(f"Tot {T}")
