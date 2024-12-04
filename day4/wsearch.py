#!/usr/bin/env python3

import numpy as np
from enum import Enum


class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)
    SE = (1, 1)
    NE = (1, -1)
    SW = (-1, 1)
    NW = (-1, -1)


def lookup(data, pos, dir, l):
    """Get the string at pos using dir and length l"""
    pos = np.array(pos)
    end = pos + np.array(dir.value) * l
    chars = ""
    idx = pos.copy()
    while True:
        # switch indexing to get x and y axis human readable
        chars += data[idx[1], idx[0]]
        idx += dir.value
        if np.all(idx == end) or np.any(idx < 0) or np.any(idx >= len(data[0])):
            break
    return chars


target = "XMAS"
data = np.genfromtxt("data1.txt", dtype=str)
data = np.array([list(s) for s in data])

count = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        for d in Direction:
            word = lookup(data, (x, y), d, len(target))
            if word == "XMAS":
                count += 1
print(count)
