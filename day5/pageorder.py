#!/usr/bin/env python3

import numpy as np
import math
from toposort import toposort, CircularDependencyError
from collections import defaultdict


graph = defaultdict(lambda: set())
candidates = []
with open("data1.txt") as f:
    for line in f.readlines():
        if "|" in line:
            x, y = [int(v) for v in line.split("|")]
            graph[y].add(x)
        elif "," in line:
            candidates.append(line)

ordering = {}
last = 0
try:
    for i, level in enumerate(toposort(graph)):
        for page in level:
            ordering[page] = i
        last = i
except CircularDependencyError as e:
    for k in e.data.keys():
        ordering[k] = last + 1


sum = 0
for c in candidates:
    c = [int(i) for i in c.strip().split(",")]
    o = np.array([ordering[i] for i in c])
    diffs = np.diff(o)
    ok = np.all(diffs > 0)
    if ok:
        sum += c[math.floor(len(c) / 2)]
print(sum)
