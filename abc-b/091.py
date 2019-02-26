#!/usr/bin/env python
# -*- conding: utf-8 -*-

N = int(input())
n = [input() for _ in range(N)]
M = int(input())
m = [input() for _ in range(M)]
l = list(set(n))
c = 0
for i in range(len(l)):
    c = max(c, n.count(l[i])-m.count(l[i]))
print(c)
