#!/usr/bin/env python3

import numpy as np
from enum import Enum


class Direction(Enum):
    # This is (row, col) or (y, x)
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


def rightof(enum_member):
    members = list(Direction)
    index = (members.index(enum_member) + 1) % len(members)
    return members[index]


def out_of_map(data, pos):
    r, c = pos
    return (r < 0) or (r >= len(data)) or (c < 0) or (c >= len(data[0]))


def move(data, pos, dir):
    while True:
        target = tuple(x + y for x, y in zip(pos, dir.value))
        if out_of_map(data, target):
            data[pos] = "X"
            break
        # print(pos, target, data[target])
        # print(data)
        if data[target] == "#":
            dir = rightof(dir)
            continue
        else:
            data[pos] = "X"
            pos = target


data = np.genfromtxt("data1.txt", dtype=str, comments=None)
data = np.array([list(s) for s in data])
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "^":
            start = (r, c)
            break
move(data, start, Direction.NORTH)
# print(data)
print(np.count_nonzero(data == "X"))
