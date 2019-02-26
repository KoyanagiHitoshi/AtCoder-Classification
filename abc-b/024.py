#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,t=map(int,input().split())
a=set()
for i in range(n):
    s=int(input())
    a=a|set(range(s,s+t))
print(len(a))


