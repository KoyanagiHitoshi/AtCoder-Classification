#!/usr/bin/env python
# -*- conding: utf-8 -*-

l=[int(_) for _ in input().split()]
k=int(input())
for i in range(k):l[l.index(max(l))]=max(l)*2
print(sum(l))
