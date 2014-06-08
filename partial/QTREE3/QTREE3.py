#!/usr/bin/env python
# coding: utf-8

def ask(goal, path):
    n = path[-1]
    if n == goal:
        if all(not nodes[v] for v in path):
            print -1
        for v in path:
            if nodes[v]:
                print v
                break
    for x in edges[n]:
        if x not in path:
            path.append(x)
            ask(goal, path)
            path.pop()

def change(v):
    nodes[v] = not nodes[v]

N, Q = map(int, raw_input().split())

nodes = [False] * (N + 1)
edges = {}

for n in range(N-1):
    a, b = map(int, raw_input().split())
    if a in edges:
        edges[a].append(b)
    else:
        edges[a] = [b]
    if b in edges:
        edges[b].append(a)
    else:
        edges[b] = [a]
for q in range(Q):
    m, v = map(int, raw_input().split())
    if m:
        ask(v, [1])
    else:
        change(v)

