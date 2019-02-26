#!/usr/bin/env python
# -*- conding: utf-8 -*-

n,k=map(int,input().split())
h=sorted([int(input()) for i in range(n)])
d=10e9
for i in range(n-k+1):
    d=min(d,h[i+k-1]-h[i])
print(d)
