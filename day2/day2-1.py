#!/usr/bin/env python3

import numpy as np


def safe(row):
    row = row[~np.isnan(row)]
    diffs = np.diff(row)
    increasing = np.all(diffs > 0)
    decreasing = np.all(diffs < 0)
    at_least_one = np.all(abs(diffs) >= 1)
    at_most_three = np.all(abs(diffs) <= 3)
    # print(row, increasing, decreasing, at_least_one, at_most_three)
    return (increasing or decreasing) and at_least_one and at_most_three


def safe_if_remove(row):
    row = row[~np.isnan(row)]
    if safe(row):
        return True
    for i in range(len(row)):
        nrow = np.delete(row, i)
        if safe(nrow):
            return True
    return False


def pad(row):
    return row + [np.nan] * (8 - len(row))


with open("data1.txt") as f:
    data = [pad([int(m) for m in l.split()]) for l in f.readlines()]
    data = np.array(data)

issafe = sum([safe(row) for row in data])
print(issafe)
issafe = sum([safe_if_remove(row) for row in data])
print(issafe)
