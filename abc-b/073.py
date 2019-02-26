#!/usr/bin/env python
# -*- conding: utf-8 -*-

n=int(input())
l=[[int(i) for i in input().split()] for _ in range(n)]
s=0
for i in range(n):
    s+=l[i][1]-l[i][0]+1
print(s)
