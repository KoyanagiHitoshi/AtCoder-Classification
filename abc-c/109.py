#!/usr/bin/env python
# -*- conding: utf-8 -*-

from fractions import gcd
n,d=map(int,input().split())
x=sorted(list(map(int,input().split()))+[d])
r=x[1]-x[0]
for i in range(n):
    r=gcd(x[i+1]-x[i],r)
print(r)
