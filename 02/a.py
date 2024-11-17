#!/usr/bin/env python3

import fileinput
import re
# counters
T = 0


ls = [line.strip() for line in fileinput.input()]


words = ls[0].split(':')[1].split(',')
script = ls[2]

for w in words:
    T += len(re.findall(w, script))

print(f"Tot {T}")
