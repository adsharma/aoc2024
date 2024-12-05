#!/usr/bin/env python3

from collections import defaultdict


graph = defaultdict(lambda: set())
candidates = []
with open("data1.txt") as f:
    for line in f.readlines():
        if "|" in line:
            x, y = [int(v) for v in line.split("|")]
            graph[y].add(x)
        elif "," in line:
            line = [int(i) for i in line.strip().split(",")]
            candidates.append(line)

incorrect = []
sum = 0
for c in candidates:
    ok = True
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if c[i] in graph and c[j] in graph[c[i]]:
                ok = False
    if ok:
        sum += c[len(c) // 2]
    else:
        incorrect.append(c)
print(sum)

# second part
sum2 = 0
for c in incorrect:
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if c[i] in graph and c[j] in graph[c[i]]:
                (c[i], c[j]) = (c[j], c[i])
    sum2 += c[len(c) // 2]
print(sum2)
