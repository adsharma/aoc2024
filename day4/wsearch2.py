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


# These assist finding the other diagonal. For example
# for SE you'd go SOUTH and then NE to find the other diagonal
corner = {
    Direction.SE: Direction.SOUTH,
    Direction.NE: Direction.NORTH,
    Direction.SW: Direction.SOUTH,
    Direction.NW: Direction.NORTH,
}
diag = {
    Direction.SE: Direction.NE,
    Direction.NE: Direction.SE,
    Direction.SW: Direction.NW,
    Direction.NW: Direction.SW,
}


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


def find_corners(pos, d, l):
    def add(p, d):
        x, y = p
        return (x + l * d.value[0], y + l * d.value[1])

    opp = add(pos, d)
    near_corner = add(pos, corner[d])
    other_corner = add(near_corner, diag[d])
    return [pos, near_corner, opp, other_corner]


target = "MAS"
data = np.genfromtxt("data1.txt", dtype=str)
data = np.array([list(s) for s in data])

ldiag = len(target) - 1
count = 0
hits = set()
for x in range(len(data)):
    for y in range(len(data[0])):
        for d in [Direction.SE, Direction.NE, Direction.SW, Direction.NW]:
            word = lookup(data, (x, y), d, len(target))
            if word == target or word == target[::-1]:
                corners = find_corners((x, y), d, ldiag)
                word2 = lookup(data, corners[1], diag[d], len(target))
                if word2 == target or word2 == target[::-1]:
                    # print(word, word2, (x, y), d)
                    hits.add(frozenset(corners))
                    count += 1

print(len(hits))
