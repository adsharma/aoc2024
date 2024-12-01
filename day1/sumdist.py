#!/usr/bin/env python3

import numpy as np
import heapq

data = np.genfromtxt("data1.txt", dtype=int)
h1, h2 = data[:, 0].tolist(), data[:, 1].tolist()

[heapq.heapify(h) for h in (h1, h2)]
total = 0
while h1 and h2:
    e1 = heapq.heappop(h1)
    e2 = heapq.heappop(h2)
    total += abs(e2 - e1)

print(total)
