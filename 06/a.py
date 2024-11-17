#!/usr/bin/env pypy3

import fileinput
from collections import defaultdict, deque

E = {}

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    o, ts = l.split(':')
    if o != 'BUG':
        E[o] = ts.split(',')


def get_paths(n: str, path: list[str]) -> list[list[str]]:
    nl = list()
    path.append(n)

    if not n in E:
        nl.append(path)
        return nl

    ts = E[n]
    for t in ts:
        paths = get_paths(t, path.copy())
        nl.extend(paths)

    return nl


def bfs(n: str) -> list[list[str]]:
    q = deque()
    q.append((n, [n]))
    paths = []

    while q:
        n, p = q.popleft()
        if n in E:
            for t in E[n]:
                pc = p.copy()
                pc.append(t)
                q.append((t, pc))
        else:
            paths.append(p)

    return paths


# paths = get_paths('RR', list())
paths = bfs('RR')
lens = defaultdict(list)
for p in paths:
    if p[-1] == '@':
        lens[len(p)].append(p)

for l, ps in lens.items():
    if len(ps) == 1:
        p = ps.pop()
        print(''.join(p))
        print(''.join([n[0] for n in p]))
        break
