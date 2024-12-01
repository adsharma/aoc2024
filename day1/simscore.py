#!/usr/bin/env python3

import numpy as np

data = np.genfromtxt("data2.txt", dtype=int)
h1, h2 = data[:, 0], data[:, 1]
elements, counts = np.unique(h2, return_counts=True)
counts_dict = dict(zip(elements, counts))

total = sum([i * counts_dict.get(i, 0) for i in h1])

print(total)
