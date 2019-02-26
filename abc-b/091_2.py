#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=[input() for _ in range(int(input()))]
m=[input() for _ in range(int(input()))]
l=list(set(n))
print(max(0,max(n.count(l[i])-m.count(l[i]) for i in range(len(l)))))
