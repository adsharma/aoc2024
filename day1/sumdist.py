#!/usr/bin/env python3

import numpy as np
import heapq

data = open("data1.txt").read()

data = np.array([x.split() for x in (data.splitlines())]).transpose()
h1, h2 = [list(map(int, x.tolist())) for x in (data[0, :], data[1, :])]
[heapq.heapify(h) for h in (h1, h2)]
total = 0
while h1 and h2:
    e1 = heapq.heappop(h1)
    e2 = heapq.heappop(h2)
    total += abs(e2 - e1)

print(total)
