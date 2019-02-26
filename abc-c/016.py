#!/usr/bin/env python
# -*- conding: utf-8 -*-

V,E=map(int,input().split())
edges=[set() for i in range(V)]
for i in range(E):
    a,b=map(int,input().split())
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)
for i in range(V):
    print(len({n for v in edges[i] for n in edges[v] if not n in edges[i] and n!=i}))
